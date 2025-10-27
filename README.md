s# 📞 Phone Info Checker

A simple Python project to check **country, carrier, and timezone information** for any phone number using the `phonenumbers` library.

---

## 🚀 Features
- Validate and format phone numbers
- Detect country, carrier, and time zone
- Save results to `results.txt`
- Simple CLI interface

---

## ⚙️ Setup Instructions

1. **Clone or download** this project folder:
   ```bash
   git clone https://github.com/yourusername/phoneinfo.git
   cd phoneinfo
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Run the Project

```bash
python main.py
```

Example:
```
📞 Phone Info Checker
Type 'exit' to quit

Type phone number with country code: +14155552671

✅ Lookup successful:

formatted: +14155552671
country_code: 1
national_number: 4155552671
region: California
carrier: AT&T Wireless
time_zones: ('America/Los_Angeles',)

Result saved to results.txt
```

---

## 🧱 Project Structure

```
phoneinfo/
├── src/
│   ├── __init__.py
│   ├── phone_info.py
│   ├── utils.py
│
├── tests/
│   └── test_phone_info.py # Optional
│
├── requirements.txt
├── README.md
└── main.py
```

---

## 🧪 Example Test
```python
from src.phone_info import get_phone_info

result = get_phone_info("+14155552671")
print(result)
```

---

## 📜 License
This project is released under the **MIT License** — feel free to modify and use it.

---
