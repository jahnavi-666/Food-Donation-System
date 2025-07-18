# 🍽️ Food Donation System

## 🌟 Project Overview

The **Food Donation System** is a web-based platform designed to reduce food waste and alleviate hunger by connecting **food donors** (like restaurants and supermarkets) with **recipients** (local charities, shelters, and individuals in need). This system encourages social responsibility while promoting sustainability and resource efficiency.

---

## 🚀 Features

1. **User Registration & Login**
   - Separate accounts for donors and recipients.
   - Secure login system for authentication.

2. **Donation Listings**
   - Donors can list available surplus food.
   - Details include: food type, quantity, expiry date, and pickup location.

3. **Search Functionality**
   - Recipients can search for nearby food donations based on location.

4. **Donation Requests**
   - Recipients can request and confirm donations.
   - Donors get notified when their food is requested.

5. **Reviews & Ratings**
   - Recipients can rate and review donors.
   - Builds trust and transparency in the donation community.

---

## 🛠️ Tech Stack

| Component         | Technology              |
|------------------|--------------------------|
| Frontend         | HTML, CSS, JavaScript    |
| Backend          | Python (Flask/Django)    |
| Database         | MySQL                    |
| Development Tool | Any Text Editor (VS Code, Sublime Text, etc.) |

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/food-donation-system.git
cd food-donation-system
````

### 2. Set up the MySQL database

* Create a database in MySQL:

```sql
CREATE DATABASE food_donation;
```

* Import schema:

```sql
USE food_donation;
SOURCE database.sql;
```

### 3. Run the application

```bash
python app.py
```

* Open your browser and go to `http://localhost:5000/`

---
