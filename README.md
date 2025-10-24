# PD: A Cross-Platform Python Orchestrator 🐍

![PD](https://img.shields.io/badge/PD-Project-blue?style=for-the-badge&logo=python)

Welcome to the **PD** repository! This project serves as a powerful cross-platform Python orchestrator designed to streamline your reconnaissance efforts. It bootstraps Go and installs essential ProjectDiscovery tools, including Subfinder, HTTPX, URLFinder, and Nuclei, along with their templates. The result? A seamless recon pipeline that outputs plain-text results for each domain you analyze.

## 🚀 Features

- **Cross-Platform Support**: Works on Windows, macOS, and Linux.
- **Automated Tool Installation**: Easily installs Subfinder, HTTPX, URLFinder, and Nuclei.
- **Streamlined Recon Pipeline**: Executes a series of tools in a defined order: Subfinder → HTTPX → URLFinder → Nuclei.
- **Plain-Text Output**: Provides clear and easy-to-read results per domain.

## 📦 Getting Started

To get started with PD, follow these steps:

1. **Download the latest release** from the [Releases section](https://github.com/dhyeygamdha/PD/releases). You will find the necessary files to download and execute.
2. **Install Dependencies**: Ensure you have Python and Go installed on your system.
3. **Run the Orchestrator**: Use the command line to execute the orchestrator.

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python** (version 3.6 or higher)
- **Go** (version 1.15 or higher)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dhyeygamdha/PD.git
   cd PD
   ```

2. **Install Required Tools**:
   The orchestrator will automatically install the necessary tools for you. Simply run:
   ```bash
   python .py
   ```

3. **Run the Recon Pipeline**:
   After installation, you can run the recon pipeline with:
   ```bash
   python orchestrator.py -d example.com
   ```

This command will initiate the pipeline for the specified domain.

## 🔧 Tools Included

### Subfinder

Subfinder is a subdomain discovery tool that helps you find valid subdomains for a target domain.

### HTTPX

HTTPX is a fast and multi-purpose HTTP toolkit that allows you to probe for working endpoints.

### URLFinder

URLFinder is a tool designed to extract URLs from web pages.

### Nuclei

Nuclei is a fast tool for targeted scanning, using templates to find vulnerabilities.

## 🌐 Topics

This repository covers a range of topics relevant to security and reconnaissance:

- Bug Bounty
- Enumeration
- Penetration Testing
- Project Discovery Tools
- Red Team Operations
- Web Application Security

## 📜 Usage

Once you have set up PD, you can use it to perform reconnaissance on any domain. Here’s a quick example:

```bash
python orchestrator.py -d targetdomain.com
```

This command will kick off the entire pipeline, and you will receive a plain-text output of your findings.

## 🎨 Customization

You can customize the pipeline by modifying the configuration file. This allows you to change the order of tools, add or remove tools, and adjust parameters to fit your needs.

## 🔗 Documentation

For detailed documentation on each tool and its parameters, refer to the official documentation:

- [Subfinder Documentation](https://projectdiscovery.io/subfinder/)
- [HTTPX Documentation](https://projectdiscovery.io/httpx/)
- [URLFinder Documentation](https://projectdiscovery.io/urlfinder/)
- [Nuclei Documentation](https://projectdiscovery.io/nuclei/)

## 📈 Contributing

We welcome contributions! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

### How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## 🛠️ Issues

If you encounter any issues while using PD, please check the [Issues section](https://github.com/dhyeygamdha/PD/issues) for existing reports or create a new issue.

## 📅 Changelog

For a detailed list of changes and updates, visit the [Releases section](https://github.com/dhyeygamdha/PD/releases). Here, you will find all the versions and their corresponding updates.

## 🤝 Acknowledgments

Special thanks to the ProjectDiscovery team for their tools and contributions to the security community. Their work makes projects like PD possible.

## 🌟 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 📞 Contact

For questions or feedback, you can reach out to the repository owner through GitHub.

---

Thank you for checking out PD! We hope it serves you well in your reconnaissance efforts. Don't forget to visit the [Releases section](https://github.com/dhyeygamdha/PD/releases) for the latest updates and tools. Happy hunting!