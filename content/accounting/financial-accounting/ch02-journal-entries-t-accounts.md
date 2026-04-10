---
chapter: 2
title: Journal Entries and T-Accounts
subject: accounting
course: financial-accounting
prefix: ACG
code: "203"
keywords: [journal entry, general journal, general ledger, T-account, posting, trial balance, source document, compound entry, journalizing]
prereqs: [ch01]
---

# Journal Entries and T-Accounts

## Overview
After analyzing transactions, accountants record them in chronological order using journal entries. A journal entry captures the date, accounts affected, debit and credit amounts, and a brief explanation. Entries are then posted (transferred) to the general ledger, where each account has its own page (often visualized as a T-account). The ledger organizes information by account rather than by date.

The recording cycle goes: Source Document -> Journal Entry -> Post to Ledger -> Trial Balance. This systematic process creates an audit trail and ensures all transactions are captured and organized for financial statement preparation.

## Key Terms
- **Journal (General Journal)**: The chronological record of all transactions. Called the "book of original entry" because transactions are first recorded here.
- **Journal Entry**: A record of a transaction in the journal, showing the date, accounts debited and credited, amounts, and a brief description.
- **Compound Journal Entry**: A journal entry involving more than two accounts (e.g., one debit and two credits, or two debits and one credit).
- **General Ledger**: The collection of all accounts used by a business. Each account has its own page showing all debits and credits. Called the "book of final entry."
- **Posting**: The process of transferring journal entry amounts to the appropriate accounts in the general ledger.
- **T-Account**: A simplified visual representation of a ledger account. The account title goes on top, debits on the left side, credits on the right side. The balance is the difference between the two sides.
- **Source Document**: The original evidence of a transaction (invoice, receipt, check, contract). Provides the basis for journal entries.
- **Footing**: Adding up the debit and credit columns of a T-account to determine the balance.
- **Cross-Referencing**: Including journal page numbers in ledger accounts and ledger account numbers in journal entries to create an audit trail.

## Core Concepts

### Journal Entry Format
```
Date    Account Debited                  Debit     Credit
        Account Credited                           Amount
        (Brief description of transaction)
```

Debited accounts are listed first, indented less. Credited accounts are listed second, indented more.

Example: March 5 -- Purchased office supplies for $500 on account.
```
Mar 5   Supplies                          500
            Accounts Payable                         500
        (Purchased office supplies on credit)
```

### Posting to T-Accounts
After recording journal entries, post each debit and credit to the appropriate T-account:

```
     Supplies                    Accounts Payable
  ──────────────              ──────────────────
  Mar 5  500 |                |  Mar 5  500
             |                |
```

Supplies (asset) has a $500 debit balance (increased). Accounts Payable (liability) has a $500 credit balance (increased).

### The Recording Process Step by Step
1. Identify the transaction from source documents
2. Analyze: Which accounts? Increase or decrease? Debit or credit?
3. Journalize: Record the entry in the general journal
4. Post: Transfer debits and credits to ledger T-accounts
5. Prepare a trial balance: List all accounts and balances; verify debits = credits

### Comprehensive Example: One Month of Transactions
Jan 1: Owner invests $30,000 cash.
  Dr. Cash 30,000 / Cr. Common Stock 30,000

Jan 3: Pay $12,000 for 12 months of rent in advance.
  Dr. Prepaid Rent 12,000 / Cr. Cash 12,000

Jan 5: Purchase equipment for $8,000 cash.
  Dr. Equipment 8,000 / Cr. Cash 8,000

Jan 10: Perform services for $5,000 on account.
  Dr. Accounts Receivable 5,000 / Cr. Service Revenue 5,000

Jan 15: Pay employee salaries $2,000.
  Dr. Salaries Expense 2,000 / Cr. Cash 2,000

Jan 20: Collect $3,000 from Jan 10 customer.
  Dr. Cash 3,000 / Cr. Accounts Receivable 3,000

Jan 25: Pay $500 utilities bill.
  Dr. Utilities Expense 500 / Cr. Cash 500

Trial Balance at Jan 31:
Debits: Cash $10,500 + AR $2,000 + Prepaid Rent $12,000 + Equipment $8,000 + Salaries Exp $2,000 + Utilities Exp $500 = $35,000
Credits: Common Stock $30,000 + Service Revenue $5,000 = $35,000
Balanced.

## Examples

### Example 1: Compound Entry
Company receives $10,000 cash from a client: $4,000 for services already performed (on account) and $6,000 as advance payment for future services.
```
Dr. Cash                  10,000
    Cr. Accounts Receivable          4,000
    Cr. Unearned Revenue             6,000
```
Three accounts, one debit and two credits. The $4,000 reduces the receivable; the $6,000 is a liability because services have not yet been performed.

### Example 2: Error Detection via Trial Balance
If a trial balance does not balance (debits do not equal credits), possible errors include:
- A journal entry with unequal debits and credits
- A posting error (wrong amount, wrong side, or omitted posting)
- An arithmetic error in footing accounts

Errors that a trial balance will NOT catch:
- Recording to the wrong account (but correct amount and side)
- Omitting an entire transaction
- Recording the wrong amount on both debit and credit sides

### Example 3: Tracing a Transaction
Source document: Invoice #4521 from Office Depot for $200 of supplies.
Journal: Dr. Supplies $200, Cr. Accounts Payable $200, Ref: Invoice #4521.
Ledger: Post $200 debit to Supplies account, $200 credit to A/P account.
Trial balance: Supplies balance increases by $200; A/P balance increases by $200.

## Relationships
- Journal entries implement the debit/credit rules from Ch. 1
- T-accounts organize entries by account for financial statement preparation
- The trial balance is the starting point for adjusting entries (Ch. 7)
- The general ledger feeds directly into the income statement (Ch. 3), balance sheet (Ch. 4), and cash flow statement (Ch. 5)
- Adjusting entries (Ch. 7) and closing entries (Ch. 8) follow the same journalizing and posting process

## Common Misconceptions
- **Journal entries must have exactly one debit and one credit**: Compound entries can have multiple debits and/or multiple credits, as long as total debits = total credits.
- **Posting changes the journal entry**: Posting is simply transferring information. The journal entry is not altered; the ledger is updated.
- **The trial balance proves accuracy**: It only proves that debits = credits. Many types of errors go undetected.
- **You should memorize journal entries**: Understanding the logic (which accounts are affected, which increase/decrease, debit or credit) is far more reliable than memorizing specific entries.

## Practice Angles
- Record journal entries for common business transactions
- Post journal entries to T-accounts and calculate balances
- Prepare a trial balance from T-account balances
- Identify and correct errors in journal entries
- Trace a transaction from source document through journal to ledger
- Record compound journal entries with multiple debits or credits
