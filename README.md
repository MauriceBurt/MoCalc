# 🧮 MoCalc – Modular Network Calculator

**MoCalc** is a Python-based CLI tool designed to help network engineers and IT pros streamline subnetting tasks, binary conversions, and quick math calculations — all from one central utility.

---

## 📍 Why I Built It

As a **Certified Network Engineer** working toward **Azure mastery**, I wanted more than just online tools — I wanted my own custom utility belt.  
MoCalc reflects how I work: modular, efficient, and always evolving.  
It’s built to support engineers like me who need quick results, repeatable logic, and room to grow.

---

## 🚧 Feature Evolution by Version

### 🔹 Version 2.0
- Introduced modular class structure: `Greeting`, `BasicCalculator`, `SubnettingCalculator`
- Created a main menu for choosing between calculators
- Personalized greeting with name input

### 🔹 Version 2.1
- Refined menu navigation and input validation
- Added restart loops for continued use or exit
- Improved user experience and logical flow

### 🔹 Version 2.2
- Global exit functionality: type `exit` at almost any point
- Added confirmation prompts for exits
- Enhanced flow between calculators and main menu

### 🔹 Version 2.3
- Added Subnetting Option A: Convert IP address to binary format
- Better prompts and validation when entering octets
- More comments for code clarity and modular planning
- Solid foundation laid for future subnetting modes

###  🔹 Version 2.4 *(Current)*
- Added Option B: Calculate total and usable hosts from a CIDR block
- Added Option C: Determine the subnet address from IP and CIDR input
- Added Option D: VLSM-based subnet planning from a base IP and multiple device counts
- Outputs include: network ID, CIDR, total hosts, usable IP range, and broadcast address
- Refined logical flow and improved user feedback handling throughout
---

## 🛠️ Who It’s For

- **Junior Network Engineers** & **students in IT/Cybersecurity**
- **Tech professionals** building internal tools
- Anyone studying for **CompTIA Net+**, **AZ-700**, or **Security+**

---

## 🗂️ What’s Next (v3.x)

- Add Subnetting Options B, C, and D (usable hosts, subnet ID, etc.)
- GUI interface using **PyQt** for interactivity
- Prepare MoCalc for **pip** packaging
- *(Optional)* Wrap with **Flask** for internal API use

---

**Built by Maurice Burt** – *Network Engineer | Python Developer | NYC*  
_“I’m not just studying tech — I’m building with it.”_
