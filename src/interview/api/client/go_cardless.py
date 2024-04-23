import asyncio
import csv
import logging

from aiohttp import ClientSession

from interview.conf import settings

logger = logging.getLogger(__name__)


async def fetch(url: str, session):
    logger.info(f'Fetching {url}')

    async with session.get(url) as response:
        response.raise_for_status()

        return await response.json()


def calculate_total_payable_amount(transactions: list, minimum_transaction_count: int,
                                   fees_discount: int) -> int:
    if transactions:
        total_payable_amount = total_fees = 0

        for transaction in transactions:
            total_payable_amount += transaction['amount']
            total_fees += transaction['fee']

        total_payable_amount -= total_fees

        if len(transactions) >= minimum_transaction_count and total_fees > 0:
            total_payable_amount += int(total_fees / 100 * fees_discount)

        return total_payable_amount
    else:
        return 0


async def main():
    async with ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            tasks = []

            merchant_ids = await fetch(f'{settings.api_base_url}/merchants', session)

            for merchant_id in merchant_ids:
                tasks.append(
                    tg.create_task(fetch(f'{settings.api_base_url}/merchants/{merchant_id}', session))
                )

    with open('payments.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(('iban', 'amount_in_pence', ))

        for task in tasks:
            result = task.result()

            transactions = result['transactions']
            discount = result['discount']
            payable_amount = calculate_total_payable_amount(
                transactions, discount['minimum_transaction_count'], discount['fees_discount']
            )

            if payable_amount > 0:
                writer.writerow((result['iban'], payable_amount, ))
