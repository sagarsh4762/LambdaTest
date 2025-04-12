```markdown
# 🧪 HerokuApp Test Automation Suite

Automated UI test suite for [HerokuApp](https://the-internet.herokuapp.com/) using **Python + Pytest + Selenium**.  
This framework covers login authentication and JavaScript alert handling, with clean reporting, parallel test execution, and secure config management.

---

## 📌 Test Scenarios

### ✅ Test Case 1: Login Page  
🔗 [`/login`](https://the-internet.herokuapp.com/login)

- ✔️ Login with valid credentials:  
  `tomsmith / SuperSecretPassword!`
- ❌ Assert errors on invalid credentials

### ✅ Test Case 2: JavaScript Alerts  
🔗 [`/javascript_alerts`](https://the-internet.herokuapp.com/javascript_alerts)

- 📢 JS Alert → Accept
- 🧐 JS Confirm → Accept/Dismiss
- ⌨️ JS Prompt → Input + Accept/Dismiss

---

## 🧰 Tech Stack

- Python 3.7+
- Pytest
- Selenium WebDriver
- Allure Reports
- python-dotenv
- pytest-xdist (for parallel runs)
- pytest-rerunfailures (retries on failure)

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/herokuapp-automation.git
cd herokuapp-automation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file at the root:

```env
USERNAME=tomsmith
PASSWORD=SuperSecretPassword!
```

---

## 🧪 Running the Tests

### Run Login Test
```bash
pytest test_login.py
```

### Run Alert Handling Test
```bash
pytest alert.py
```

---

## ⚡ Advanced Features

### Parallel Execution
```bash
pytest -n auto
```

### Rerun Failed Tests
```bash
pytest --reruns 2
```

### Generate Allure Reports
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🔐 Security Best Practices

- ✅ Credentials stored in `.env` files
- ✅ No hardcoded secrets
- ✅ `.env` and `credentials.env` are gitignored

---

## 📊 Folder Structure

```
📁 allure-results/     → Allure test reports
📁 assets/             → Test assets or resources
📁 results/            → Test output and logs
🔐 .env                → Secure env config
🔐 credentials.env     → Login credentials
📄 alert.py            → JavaScript alerts automation
📄 test_login.py       → Login test logic
📄 requirements.txt    → Dependency list
```

---

## ✅ Evaluation Checklist

- ✅ Reusable Test Framework
- ✅ Clean Allure Reports
- ✅ Pytest + Selenium Integration
- ✅ Parallel Test Execution
- ✅ Auto-Reruns for Failures
- ✅ Secrets Management with `.env`

---

## 🤝 Contributing

Open an issue, fork the repo, or submit a PR — collaboration is welcome!

---

> 🧠 *"Automation is good, so long as you know exactly where to put the machine."* – Eliyahu Goldratt

```
