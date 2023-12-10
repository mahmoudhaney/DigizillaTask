# `Odoo` (v16 community) Custome Module

## Description
1. Create a model with the name "Digizilla" as follows:
    - Views: Kanban, Form and List
    - Fields:
      - Name*
      - Gender
      - Country
      - Joining Date
      - Tags
      - Customers (where you can select multiple values from `Odoo` default customers model)
      - Company* (where you can select one value from `Odoo` default Companies official model).
      - Notes (a long text field in a new tab named Notes).
      - Comments (a short text field in a new tab named Comments).
2. Your new module should have a “Messages and logger that tracks any change in the previous fields” in the form view.
    > ⚠ Hide the create button from the form view using javascript. 
3. Generate a PDF report for your model that contains all the previous fields excluding the message logger.

## Main Technologies
- `Python`
- `Odoo`
- `PostgreSQL`


## Setup

- Clone the repository using the command below:
```bash
git clone git@github.com:mahmoudhaney/DigizillaTask.git

```

- Rename the project directory to `digizilla` 

- Navigate to the directory `addons` in your installed Odoo and put the renamed directory `digizilla` in it.
```bash
odoo16\server\odoo\addons

```

- Run your Odoo server

- In your Odoo Apps dashboard search for `digizilla` app and then install it.

- Then you can use the app like in the **Demo** below.

> ⚠ You have to install `Odoo` First

## Demo
https://github.com/mahmoudhaney/DigizillaTask/assets/83553963/aa9f4ce6-2215-4fa3-a0ee-168290c011fc


## Copyrights
> ⚠ Copyright ©2023 All rights reserved

