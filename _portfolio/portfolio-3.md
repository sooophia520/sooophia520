---
title: "Java Cake Shop Member Recharge and Management System"
excerpt: "Under the guidance of teachers, develop a Java-based recharge system that implements member registration, recharge, consumption, and inquiry functions. Later, extend and deploy it as a Web application, adding an administrator terminal and a member terminal<br/><img src='/sooophia520/images/cake_shop_front_page.png'>"
collection: portfolio
---

## Project background

A cake shop keeps a running balance for each member: customers top up in advance and then spend that balance in store. Tracking it on paper means two records that disagree, so the brief was a system where registration, recharge, consumption and balance inquiry all run off the same account record. It started as a console program and was later extended into a web application with two separate entrances.

## What I built

- **Member and balance module.** Registration, recharge, consumption and balance inquiry, all reading and writing a single balance record so the numbers stay consistent.
- **Value checking.** Recharges and deductions are validated before they touch the balance, so a bad amount is rejected rather than written into the account.
- **Administrator terminal.** A separate admin login for managing members and reviewing recharge and consumption records.
- **Member terminal.** Members sign in with their own account to check balance and history, kept apart from the admin entrance.
- **Web deployment.** Extended the console version into a web application, keeping the same data and business rules behind the new interface, then deployed and tested it locally.

## Outcome

The system runs end to end: a member registers, tops up, spends part of the balance and
queries what is left, while the administrator sees the same transactions from the other
side. The two entrances are clearly split, so an admin cannot wander into the member pages
and a member never lands on the admin login by mistake.

![Administrator login page](/sooophia520/images/cake_shop_front_page.png)
