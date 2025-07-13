# Air Force Ones Price Tracker 👟📉

A Python script that monitors the price of Air Force Ones shoes on eBay and sends you an email alert when the price drops below your budget!

---

## 🔍 Overview

This script scrapes the eBay listing page for Air Force Ones shoes, extracts the current price, and compares it to your predefined budget. If the price is equal to or less than your budget, it automatically sends an email notification with the item link.

The check runs every 24 hours to keep you updated without constant manual checking.

---

## ⚙️ Features

- Scrapes the Air Force Ones eBay listing for the latest price  
- Compares the price against your budget  
- Sends an HTML email alert when the price drops below or equals your budget  
- Uses `replit.db` to prevent duplicate notifications for the same price  
- Scheduled to run automatically every 24 hours using the `schedule` module  

---

## 🚨 Prerequisites

- Python 3.6 or newer  
- Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833) enabled if using two-factor authentication  
- Python packages:

  ```bash
  pip install requests beautifulsoup4 schedule replit
