# Sekiryu v0.0.2

This Ghidra Toolkit is a comprehensive suite of tools designed to streamline and automate various tasks associated with running Ghidra in Headless mode. This toolkit provides a wide range of scripts that can be executed both inside and alongside Ghidra, enabling users to perform tasks such as Vulnerability Hunting, Pseudo-code Commenting with ChatGPT and Reporting with Data Visualization on the analyzed codebase.

## Key Features

- **Headless Mode Automation**: The toolkit enables users to seamlessly launch and run Ghidra in Headless mode, allowing for automated and batch processing of code analysis tasks.

- **Script Repository**: The toolkit includes a repository of pre-built scripts that can be executed within Ghidra. These scripts cover a variety of functionalities, empowering users to perform diverse analysis and manipulation tasks.

- **Vulnerability Hunting**: Leverage the toolkit's scripts to identify potential vulnerabilities within the codebase being analyzed. This helps security researchers and developers uncover security weaknesses and proactively address them.

- **Automatic Pseudo Code Generating**: Automatically generate pseudo code within Ghidra's Headless mode. This feature assists in understanding and documenting the code logic without manual intervention.

- **Pseudo-code Commenting with ChatGPT**: Enhance the readability and understanding of the codebase by utilizing ChatGPT to generate human-like comments for pseudo-code snippets. This feature assists in documenting and explaining the code logic.

- **Reporting and Data Visualization**: Generate comprehensive reports with visualizations to summarize and present the analysis results effectively. The toolkit provides data visualization capabilities to aid in identifying patterns, dependencies, and anomalies in the codebase.

- **Script Management**: The toolkit allows users to load and save their own scripts, providing flexibility and customization options for their specific analysis requirements. Users can easily manage and organize their script collection.

- **Flexible Input Options**: Users can utilize the toolkit to analyze individual files or entire folders containing multiple files. This flexibility enables efficient analysis of both small-scale and large-scale codebases.

  
# Pre-requisites

Before using this project, make sure you have the following software installed:

- Ghidra: You can download Ghidra from the National Security Agency's GitHub repository @  https://github.com/NationalSecurityAgency/ghidra
- Ghidrathon: Get the Ghidrathon plugin from the mandiant GitHub repository @ https://github.com/mandiant/Ghidrathon
- Java: Make sure you have Java Development Kit (JDK) version 17 or higher installed. You can download it from the OpenJDK website @ https://openjdk.org/projects/jdk/17/
    
# Warning
 
    The xmlrpc.server module is not secure against maliciously constructed data. If you need to parse 
    untrusted or unauthenticated data see XML vulnerabilities. 

For more information about Bushido Security, please visit our website: https://www.bushido-sec.com/.
