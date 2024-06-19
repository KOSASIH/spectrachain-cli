import argparse
import os
from rich.console import Console
from rich.table import Table

console = Console()

def display_transaction_table(transactions: list) -> None:
    table = Table(title='Transactions')
    table.add_column('ID', style='cyan')
    table.add_column('From', style='magenta')
    table.add_column('To', style='green')
    table.add_column('Value', style='yellow')
    for transaction in transactions:
        table.add_row(transaction['id'], transaction['from'], transaction['to'], transaction['value'])
    console.print(table)

def main():
    parser = argparse.ArgumentParser(description='SpectraChain CLI')
    parser.add_argument('--get-transactions', action='store_true', help='Get latest transactions')
    parser.add_argument('--analyze-transaction', type=str, help='Analyze a specific transaction')
    args = parser.parse_args()

    if args.get_transactions:
        # Fetch latest transactions from blockchain
        #...
        display_transaction_table(transactions)
    elif args.analyze_transaction:
        # Analyze transaction using AI-powered model
        #...
        console.print(f'Transaction risk: {risk:.2f}')

if __name__ == '__main__':
    main()
