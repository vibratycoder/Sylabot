# ISA 311: Introduction to Cybersecurity - Flashcard Reference Bank

---

## SQL Injection

### Key Terms & Definitions
- **SQL Injection (SQLi)**: A web security vulnerability where an attacker injects malicious SQL code into application queries to manipulate a database
- **In-Band SQLi**: Attack where the attacker uses the same communication channel to launch the attack and retrieve results
- **Blind SQLi**: Attack where the attacker infers information from application behavior (true/false responses) without seeing direct query output
- **UNION-Based SQLi**: Technique that uses the SQL UNION operator to combine results from injected queries with the original query to extract data from other tables
- **Error-Based SQLi**: Technique that forces the database to generate error messages containing sensitive information
- **Out-of-Band SQLi**: Attack that uses different communication channels (e.g., DNS or HTTP requests) to exfiltrate data; harder to execute
- **Parameterized Query**: A prepared SQL statement where user input is treated as data, not executable code, preventing injection
- **Prepared Statement**: A precompiled SQL template that separates code from data, the primary defense against SQLi
- **Input Validation**: The process of checking user-supplied data against an allow-list of acceptable values before processing
- **Least-Privilege Access**: Database security principle where accounts are given only the minimum permissions necessary to perform their function

### Core Concepts (Q&A Format)
- Q: What is the difference between in-band and blind SQL injection?
- A: In-band SQLi returns results directly through the same channel (e.g., the web page), while blind SQLi does not show results -- the attacker must infer data from application behavior like true/false responses or time delays.

- Q: Why are parameterized queries the most effective defense against SQL injection?
- A: Parameterized queries separate SQL code from user input so the database treats input strictly as data values, never as executable SQL commands, regardless of what the user enters.

- Q: How does a UNION-based SQL injection attack work?
- A: The attacker appends a UNION SELECT statement to the original query, combining the legitimate results with data from other database tables, allowing extraction of information the application was not intended to reveal.

- Q: What is the impact of a successful SQL injection attack?
- A: Attackers can read, modify, or delete database data; bypass authentication; access other users' records; and in severe cases escalate to full server compromise or OS command execution.

- Q: Why should database error messages not be exposed to end users?
- A: Detailed error messages reveal database structure, table names, and column types, giving attackers the information they need to craft more precise injection attacks.

- Q: Where does SQL injection rank on the OWASP Top 10?
- A: Injection (including SQLi) ranks #5 on the OWASP Top 10 (2025) and has consistently appeared in the Top 10 since its inception.

### Important Facts & Figures
- SQL injection has been in the OWASP Top 10 since the list was first published in 2003
- A single unparameterized query can expose an entire database to attack
- SQLi can lead to complete system compromise, not just data theft
- The three main categories are: In-Band, Blind/Inferential, and Out-of-Band
- Error-based SQLi exploits verbose database error messages to extract data
- Time-based blind SQLi uses SQL commands like SLEEP() or WAITFOR DELAY to infer true/false answers from response timing
- Second-order SQLi stores malicious input that executes later when used in a different query
- Defense-in-depth for SQLi includes parameterized queries + input validation + least privilege + WAF (Web Application Firewall)

### Common Exam Questions
- Q: Which type of SQLi uses the same channel for attack and data retrieval? A: In-band SQL injection.
- Q: What is the primary programmatic defense against SQL injection? A: Parameterized queries (prepared statements).
- Q: An attacker submits `' OR 1=1 --` in a login field. What type of attack is this? A: SQL injection -- the payload bypasses authentication by making the WHERE clause always true and commenting out the rest of the query.
- Q: Name three impacts of a successful SQL injection attack. A: Unauthorized data access, data modification/deletion, authentication bypass, and potentially full system compromise.
- Q: What is blind SQL injection? A: A type of SQLi where results are not directly visible; the attacker infers data by observing differences in application behavior (boolean-based) or response time (time-based).

---

## Cross-Site Scripting (XSS)

### Key Terms & Definitions
- **Cross-Site Scripting (XSS)**: An injection attack where malicious scripts are injected into trusted websites and executed in a victim's browser
- **Reflected XSS**: Malicious script is included in the current HTTP request and immediately reflected back in the response (non-persistent)
- **Stored XSS**: Malicious script is permanently saved in the target's database and served to all visitors (persistent, most dangerous)
- **DOM-Based XSS**: Vulnerability exists in client-side JavaScript that modifies the DOM, with no server-side involvement
- **Output Encoding**: Converting special characters (e.g., `<` to `&lt;`) before rendering them in HTML to prevent script execution
- **Content Security Policy (CSP)**: An HTTP header that restricts which scripts the browser is allowed to execute, mitigating XSS impact
- **HttpOnly Flag**: A cookie attribute that prevents JavaScript from accessing the cookie, defending against session hijacking via XSS
- **HTML Sanitization**: The process of cleaning user input by removing or neutralizing potentially dangerous HTML tags and attributes (e.g., using DOMPurify)
- **Session Hijacking**: Stealing a user's session token via XSS to impersonate them
- **Trusted Types**: A browser API that enforces type checking on DOM manipulation to prevent DOM-based XSS

### Core Concepts (Q&A Format)
- Q: What is the difference between reflected and stored XSS?
- A: Reflected XSS is delivered via a crafted URL and only affects users who click it (non-persistent). Stored XSS is saved in the database and automatically executes for every user who views the affected page (persistent).

- Q: Why is stored XSS considered more dangerous than reflected XSS?
- A: Stored XSS affects all users who visit the compromised page without any special interaction, while reflected XSS requires the victim to click a malicious link.

- Q: How does a Content Security Policy (CSP) help prevent XSS?
- A: CSP tells the browser which sources of scripts are trusted. Even if an attacker injects a script, the browser will refuse to execute it if the source is not whitelisted in the CSP header.

- Q: What is DOM-based XSS and how does it differ from other types?
- A: DOM-based XSS occurs entirely in the client-side JavaScript when it unsafely writes user input into the DOM. The malicious payload never reaches the server, making it harder to detect with server-side defenses.

- Q: What is the purpose of the HttpOnly cookie flag in XSS defense?
- A: It prevents client-side JavaScript from reading cookies, so even if an XSS attack executes, it cannot steal session tokens stored in HttpOnly cookies.

- Q: Name three consequences of a successful XSS attack.
- A: Session hijacking (account takeover), phishing (displaying fake login forms), keylogging, defacement, and sensitive data exposure.

### Important Facts & Figures
- XSS was first identified as a significant threat by CERT/CC in 2000
- DOM-based XSS was formally identified by Amit Klein in 2005
- There are three main types: Reflected, Stored, and DOM-based
- XSS consistently appears in the OWASP Top 10 (categorized under Injection in 2025)
- The primary defenses are: output encoding, HTML sanitization, CSP headers, and HttpOnly cookies
- Reflected XSS is the most common type; Stored XSS is the most dangerous
- Context-specific encoding is required: HTML entity encoding, JavaScript escaping, CSS escaping, and URL/percent encoding each apply in different output contexts
- XSS can be used to deliver drive-by downloads, mine cryptocurrency, or redirect users to malicious sites

### Common Exam Questions
- Q: Which type of XSS stores the malicious payload in the web application's database? A: Stored (persistent) XSS.
- Q: What HTTP header helps mitigate the impact of XSS by restricting script sources? A: Content Security Policy (CSP).
- Q: A user clicks a link containing `<script>alert('XSS')</script>` in a URL parameter, and the script executes. What type of XSS is this? A: Reflected XSS.
- Q: What is the primary defense technique against XSS in HTML output? A: Output encoding (converting special characters like < > & " to their HTML entity equivalents).
- Q: How does the HttpOnly flag protect against XSS-based session hijacking? A: It prevents JavaScript from accessing the cookie, so an XSS payload cannot read or exfiltrate the session token.

---

## Mobile Security

### Key Terms & Definitions
- **Mobile Device Management (MDM)**: Enterprise software that remotely manages, monitors, and secures employees' mobile devices, enforcing security policies
- **BYOD (Bring Your Own Device)**: Policy allowing employees to use personal devices for work, introducing additional security risks
- **COPE (Corporate-Owned, Personally Enabled)**: Model where the company owns the device but allows personal use, giving IT greater control
- **SMiShing**: Phishing attacks delivered via SMS text messages to trick users into clicking malicious links
- **Man-in-the-Middle (MitM) Attack**: Interception of communication between two parties, common on unsecured Wi-Fi networks
- **Mobile Ransomware**: Malware that locks a mobile device or encrypts its data and demands payment for restoration
- **Remote Wipe**: MDM capability to erase all data on a lost or stolen device to prevent data exposure
- **Containerization**: Separating work and personal data on a device with different security zones and passwords
- **Network Access Control (NAC)**: Solution that checks device security compliance before allowing connection to the corporate network
- **Zero-Trust Architecture**: Security model requiring continuous verification of every user and device, never assuming trust based on network location

### Core Concepts (Q&A Format)
- Q: What is the difference between BYOD and COPE deployment models?
- A: In BYOD, employees use personal devices for work (less IT control). In COPE, the company owns the device but permits personal use (greater IT control and security enforcement).

- Q: How does MDM protect corporate data on mobile devices?
- A: MDM enforces encryption, automates security patches, controls app installations, and can remotely wipe devices that are lost, stolen, or non-compliant.

- Q: What is containerization in mobile security?
- A: It creates separate encrypted zones on a device -- one for corporate data and one for personal data -- so IT can manage and wipe corporate data without affecting personal content.

- Q: Why are public Wi-Fi networks a mobile security risk?
- A: Attackers can perform Man-in-the-Middle attacks on unsecured Wi-Fi, intercepting unencrypted communications, login credentials, and sensitive data transmitted by connected devices.

- Q: What is zero-trust architecture and why is it important for mobile security?
- A: Zero-trust assumes no device or user is inherently trustworthy. Every access request is verified regardless of location, which is critical for mobile/remote workers who connect from diverse and potentially insecure networks.

- Q: What is SMiShing and how does it differ from traditional phishing?
- A: SMiShing delivers phishing attacks through SMS text messages instead of email, exploiting the trust users place in text messages and the smaller screen that makes URL inspection harder.

### Important Facts & Figures
- Information security analyst roles are projected to grow 33% from 2023 to 2033 (U.S. Bureau of Labor Statistics)
- NIST and NSA publish mobile device security best practices that guide enterprise policies
- Top mobile threats: malicious apps, phishing/SMiShing, MitM attacks, ransomware, spyware, and data leaks
- MDM core capabilities: remote wipe, encryption enforcement, automated patching, app control, and GPS tracking
- 60% of mobile users browse with just one hand, impacting security UX decisions
- BYOD risks include: data leakage, unsecured Wi-Fi, mixing personal and corporate data, lost/stolen devices, and shadow IT
- Multi-Factor Authentication (MFA) is recommended for all mobile access to corporate resources
- Mobile malware increased significantly with the rise of app sideloading outside official app stores

### Common Exam Questions
- Q: What MDM feature allows IT to protect data on a lost device? A: Remote wipe -- IT can erase all corporate data remotely.
- Q: Name three BYOD security risks. A: Data leakage, unsecured Wi-Fi connections, mixing personal/corporate data, lost/stolen devices, and unpatched vulnerabilities.
- Q: What is the purpose of containerization on a mobile device? A: To separate corporate and personal data into isolated zones so IT can manage corporate data without accessing personal content.
- Q: What does zero-trust architecture require before granting access? A: Continuous verification of user identity and device security posture, regardless of network location.
- Q: What is SMiShing? A: A phishing attack delivered via SMS text messages, designed to trick users into revealing credentials or installing malware.

---

## Encryption

### Key Terms & Definitions
- **Symmetric Encryption**: Uses a single shared key for both encryption and decryption; fast and efficient for large data volumes
- **Asymmetric Encryption**: Uses a key pair (public key to encrypt, private key to decrypt); more secure for key exchange but slower
- **AES (Advanced Encryption Standard)**: The dominant symmetric algorithm; 128-bit block cipher supporting 128, 192, and 256-bit keys; replaced DES
- **RSA (Rivest-Shamir-Adleman)**: The most widely used asymmetric algorithm; based on the difficulty of factoring large prime numbers
- **DES (Data Encryption Standard)**: Obsolete symmetric algorithm with a 56-bit key and 64-bit block size; easily brute-forced today
- **3DES (Triple DES)**: Applies DES three times with up to 168-bit key length (effective security ~112 bits); deprecated in favor of AES
- **ECC (Elliptic Curve Cryptography)**: Asymmetric algorithm providing equivalent security to RSA with much shorter key lengths
- **Diffie-Hellman**: Key exchange protocol that allows two parties to establish a shared secret over an insecure channel
- **Hybrid Encryption**: Combines asymmetric encryption (to exchange a symmetric key) with symmetric encryption (to encrypt data); used in TLS/HTTPS
- **Plaintext/Ciphertext**: Plaintext is readable data before encryption; ciphertext is the unreadable output after encryption
- **Key Length**: The size of the encryption key in bits; longer keys provide stronger security against brute-force attacks

### Core Concepts (Q&A Format)
- Q: Why is symmetric encryption faster than asymmetric encryption?
- A: Symmetric algorithms use simpler mathematical operations (substitution/permutation) with a single key, while asymmetric algorithms rely on computationally intensive operations like factoring large prime numbers.

- Q: How does hybrid encryption work in HTTPS/TLS?
- A: Asymmetric encryption (e.g., RSA) securely exchanges a symmetric session key between client and server. Then symmetric encryption (e.g., AES) encrypts all subsequent data, combining the security of asymmetric with the speed of symmetric.

- Q: Why was AES developed to replace DES?
- A: DES uses only a 56-bit key, which can be brute-forced in hours with modern hardware. AES supports 128/192/256-bit keys and uses 128-bit blocks, providing vastly stronger security and better performance.

- Q: What is the difference between AES and 3DES?
- A: AES uses 128-bit blocks and 128/192/256-bit keys with substitution-permutation design. 3DES uses 64-bit blocks and up to 168-bit keys (112-bit effective) with a Feistel network. AES is faster, more secure, and more efficient.

- Q: When would you use asymmetric vs. symmetric encryption?
- A: Use asymmetric for key exchange, digital signatures, and authentication (small data). Use symmetric for encrypting large volumes of data like files, databases, and VPN traffic.

- Q: What makes RSA secure?
- A: RSA security depends on the computational difficulty of factoring the product of two very large prime numbers.

- Q: What advantage does ECC have over RSA?
- A: ECC provides equivalent security to RSA with much shorter key lengths (e.g., a 256-bit ECC key offers similar security to a 3072-bit RSA key), making it faster and more efficient.

### Important Facts & Figures
- AES block size: 128 bits; key sizes: 128, 192, or 256 bits
- DES key size: 56 bits; block size: 64 bits -- considered insecure since the late 1990s
- 3DES effective security: ~112 bits (despite 168-bit key length); officially deprecated
- AES uses substitution-permutation network; DES/3DES use Feistel network structure
- RSA key sizes typically range from 2048 to 4096 bits for modern security
- HTTPS uses hybrid encryption: asymmetric for key exchange, then AES for data
- AES-256 is approved for U.S. government TOP SECRET classification
- Symmetric encryption is roughly 1000x faster than asymmetric encryption
- Diffie-Hellman enables secure key exchange but does not itself encrypt data

### Common Exam Questions
- Q: What type of encryption uses one key for both encryption and decryption? A: Symmetric encryption.
- Q: AES supports which key lengths? A: 128, 192, and 256 bits.
- Q: Why is DES no longer considered secure? A: Its 56-bit key can be brute-forced in hours with modern computing power.
- Q: What is the primary advantage of asymmetric encryption over symmetric? A: It eliminates the need to securely share a secret key -- the public key can be freely distributed.
- Q: In TLS, how are symmetric and asymmetric encryption used together? A: Asymmetric encryption securely exchanges a symmetric session key, which is then used to encrypt all data in the session (hybrid encryption).

---

## Virtual Labs

### Key Terms & Definitions
- **Virtual Lab**: A software-based, isolated environment that simulates real IT infrastructure for hands-on cybersecurity training without risking production systems
- **Capture the Flag (CTF)**: A gamified cybersecurity competition where participants solve security challenges to find hidden "flags" (text strings)
- **TryHackMe**: A browser-based cybersecurity training platform with guided, gamified learning paths; beginner-friendly with step-by-step instruction
- **Hack The Box (HTB)**: An advanced penetration testing platform offering CTF challenges, cyber ranges, and industry-recognized certifications
- **Cyber Range**: A simulated network environment used for realistic cybersecurity exercises including attack and defense scenarios
- **Sandboxed Environment**: An isolated computing space where code or attacks can be executed safely without affecting real systems
- **Penetration Testing (Pen Testing)**: Authorized simulated attacks on systems to identify vulnerabilities before real attackers do
- **Gamification**: Using game elements (points, levels, leaderboards) in training to increase engagement and motivation

### Core Concepts (Q&A Format)
- Q: Why are virtual labs important for cybersecurity education?
- A: They provide safe environments to practice real-world attack and defense techniques without risking damage to production networks, data, or revenue.

- Q: What is the difference between TryHackMe and Hack The Box?
- A: TryHackMe is beginner-oriented with guided, step-by-step browser-based labs. Hack The Box targets intermediate-to-advanced users with less guidance and more realistic challenges, plus industry-recognized certifications.

- Q: What is a CTF competition?
- A: A Capture the Flag competition presents cybersecurity challenges (cryptography, web exploitation, reverse engineering, etc.) where participants find hidden text strings ("flags") to earn points.

- Q: How do virtual labs replicate real-world scenarios?
- A: They simulate realistic networks, servers, and applications with intentional vulnerabilities, allowing students to practice the same techniques (reconnaissance, exploitation, remediation) used by professional security analysts.

- Q: Why is gamification effective in cybersecurity training?
- A: Points, leaderboards, and progressive difficulty maintain motivation and engagement, encouraging repeated practice and deeper exploration of security concepts.

### Important Facts & Figures
- Information security analyst roles projected to grow 33% from 2023-2033 (BLS)
- TryHackMe uses browser-based labs requiring no VPN or local VM setup
- Hack The Box offers industry-recognized professional certifications
- CTF categories typically include: web exploitation, cryptography, reverse engineering, forensics, and binary exploitation
- Virtual labs enable remote access from any location with internet connectivity
- Popular platforms: TryHackMe, Hack The Box, CyberRange, ACI Learning, Immersive Labs
- Labs allow students to practice with real tools (Nmap, Burp Suite, Metasploit, Wireshark) safely
- Employers increasingly require hands-on lab experience alongside traditional certifications

### Common Exam Questions
- Q: What is the primary benefit of virtual cybersecurity labs over textbook learning? A: They provide hands-on, practical experience with real tools and techniques in a safe environment that cannot damage production systems.
- Q: What does CTF stand for, and what is its purpose? A: Capture the Flag -- a gamified competition where participants solve security challenges to find hidden flags, building practical skills.
- Q: Name two major cybersecurity training platforms and their key differences. A: TryHackMe (beginner-friendly, guided, browser-based) and Hack The Box (advanced, less guided, professional certifications).
- Q: Why are virtual labs critical for the cybersecurity workforce? A: The field is growing 33% by 2033, and employers demand hands-on skills that can only be developed through practical lab experience.

---

## Threat Analysis

### Key Terms & Definitions
- **Threat Analysis**: A structured process of identifying, assessing, and prioritizing cybersecurity threats based on adversary behavior, attack techniques, and business impact
- **Threat Modeling**: A proactive exercise to systematically identify potential threats and attack vectors for a system before they are exploited
- **STRIDE**: Microsoft's threat classification model -- Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
- **MITRE ATT&CK**: A globally accessible knowledge base of adversary tactics and techniques based on real-world observations; organized into 14 tactical stages
- **PASTA (Process for Attack Simulation and Threat Analysis)**: A seven-stage risk-centric threat modeling methodology
- **OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation)**: A risk assessment framework developed by Carnegie Mellon's CERT
- **Risk Formula**: Risk = Impact (Damage Potential) x Likelihood (Probability of occurrence)
- **Quantitative Risk Assessment**: Uses numerical data, monetary values, and statistical models to calculate risk
- **Qualitative Risk Assessment**: Uses expert judgment, categories (High/Medium/Low), and descriptive scales to evaluate risk
- **Attack Surface**: The total number of points where an unauthorized user could attempt to enter or extract data from a system

### Core Concepts (Q&A Format)
- Q: What does each letter in STRIDE represent?
- A: Spoofing (faking identity), Tampering (modifying data), Repudiation (denying actions), Information Disclosure (exposing data), Denial of Service (disrupting availability), Elevation of Privilege (gaining unauthorized access).

- Q: How is MITRE ATT&CK organized?
- A: It breaks cyberattack lifecycles into 14 tactical stages (e.g., Initial Access, Execution, Persistence, Privilege Escalation, Exfiltration). Each tactic contains specific techniques and sub-techniques observed in real attacks.

- Q: What is the risk formula used in threat analysis?
- A: Risk = Damage Potential (Impact) x Likelihood (Probability). A high-impact, high-probability threat receives the highest risk rating.

- Q: What is the difference between quantitative and qualitative risk assessment?
- A: Quantitative uses numerical values and financial metrics (e.g., Annual Loss Expectancy). Qualitative uses descriptive categories (High/Medium/Low) based on expert judgment. Most organizations use a combination of both.

- Q: How do STRIDE and MITRE ATT&CK complement each other?
- A: STRIDE provides high-level threat categories for initial modeling, while ATT&CK provides detailed, specific techniques attackers actually use. STRIDE identifies what could go wrong; ATT&CK shows how attackers do it.

- Q: What are the basic steps of the threat analysis process?
- A: (1) Identify assets, (2) enumerate threats, (3) assess vulnerabilities, (4) calculate risk ratings, (5) develop and prioritize mitigation strategies.

### Important Facts & Figures
- STRIDE was originally developed by Microsoft employees Loren Kohnfelder and Praerit Garg
- MITRE ATT&CK contains 14 tactical stages covering the full cyberattack lifecycle
- MITRE ATT&CK is based on real-world observations of adversary behavior, not theoretical threats
- PASTA is a seven-stage methodology; OCTAVE was developed by Carnegie Mellon's CERT division
- Risk ranking: highest priority = high impact + high likelihood; lowest = low impact + low likelihood
- Threat modeling should occur during the design phase of system development (shift-left security)
- The four main threat modeling questions: (1) What are we building? (2) What can go wrong? (3) What are we going to do about it? (4) Did we do a good enough job?
- MITRE ATT&CK is freely available at attack.mitre.org and used by both government and private sector

### Common Exam Questions
- Q: What does the "S" in STRIDE stand for? A: Spoofing -- pretending to be someone or something else.
- Q: What is the risk formula? A: Risk = Impact x Likelihood.
- Q: What is MITRE ATT&CK? A: A globally accessible, real-world-based knowledge base of adversary tactics and techniques organized into 14 stages of the cyberattack lifecycle.
- Q: Name the difference between quantitative and qualitative risk assessment. A: Quantitative uses numerical/monetary values; qualitative uses descriptive categories (High/Medium/Low) and expert judgment.
- Q: In what phase of development should threat modeling ideally occur? A: During the design phase (shift-left security), before code is written, to identify and address threats early.

---

## Security Vulnerabilities

### Key Terms & Definitions
- **Security Vulnerability**: A flaw or weakness in software design or implementation that an attacker can exploit to cause harm
- **OWASP Top 10**: The industry-standard awareness document listing the ten most critical web application security risks, updated periodically
- **CVE (Common Vulnerabilities and Exposures)**: A global identification system that assigns unique IDs (e.g., CVE-2024-12345) to known security vulnerabilities
- **CWE (Common Weakness Enumeration)**: A classification system for the types of software weaknesses that lead to vulnerabilities
- **Broken Access Control**: OWASP #1 (2025) -- failures in enforcing user permissions, allowing unauthorized actions
- **Security Misconfiguration**: OWASP #2 (2025) -- insecure default settings, open cloud storage, unnecessary features enabled
- **Cryptographic Failures**: OWASP #3 (2025) -- weak encryption, exposed sensitive data, improper certificate validation
- **Vulnerable Components**: OWASP #4 (2025) -- using outdated or known-vulnerable third-party libraries and frameworks
- **Injection**: OWASP #5 (2025) -- attacker-supplied data is executed as code (SQLi, XSS, command injection)
- **Zero-Day Vulnerability**: A vulnerability unknown to the vendor with no available patch, actively exploited by attackers
- **Patch Management**: The process of regularly applying security updates to fix known vulnerabilities

### Core Concepts (Q&A Format)
- Q: What is the relationship between CVE and CWE?
- A: CWE classifies types of software weaknesses (the root cause). CVE identifies specific instances of vulnerabilities in real software products. A single CWE category can map to many CVEs.

- Q: What is the OWASP Top 10 and why is it important?
- A: It is the industry-standard document listing the ten most critical web application security risks. It guides developers and security professionals on the most important vulnerabilities to address and is used in compliance frameworks worldwide.

- Q: What is Broken Access Control and why is it ranked #1?
- A: It occurs when users can act outside their intended permissions (e.g., accessing other users' data, modifying records they shouldn't). It is #1 because it is the most commonly found critical vulnerability in web applications.

- Q: What is a zero-day vulnerability?
- A: A security flaw unknown to the software vendor with no patch available. "Zero-day" means the vendor has had zero days to fix it, making it extremely dangerous when actively exploited.

- Q: How do the OWASP Top 10 and CWE relate?
- A: Each OWASP Top 10 category maps to multiple CWEs. For example, the Injection category includes CWEs for SQL injection, XSS, command injection, and others.

- Q: What is the difference between a vulnerability and an exploit?
- A: A vulnerability is a weakness in a system. An exploit is the actual technique or code used to take advantage of that vulnerability.

- Q: What is new in the OWASP Top 10:2025?
- A: A10:2025 "Mishandling of Exceptional Conditions" is a new category covering improper error handling, logical errors, and failing open, containing 24 CWEs.

### Important Facts & Figures
- OWASP Top 10 (2025): #1 Broken Access Control, #2 Security Misconfiguration, #3 Cryptographic Failures, #4 Vulnerable Components, #5 Injection
- The CVE system is maintained by MITRE Corporation and sponsored by the U.S. Department of Homeland Security
- CWE is also maintained by MITRE and funded by DHS CISA
- A10:2025 "Mishandling of Exceptional Conditions" is a new category with 24 mapped CWEs
- The Injection category (#5) has the greatest number of associated CVEs among the OWASP Top 10
- OWASP Top 10 was first published in 2003 and is updated approximately every 3-4 years
- Not all CWEs have known exploits or CVEs, but scanning for OWASP-mapped CWEs significantly reduces risk
- Security vulnerabilities can exist in custom code, third-party libraries, frameworks, operating systems, and network configurations

### Common Exam Questions
- Q: What is the #1 vulnerability in the OWASP Top 10:2025? A: Broken Access Control.
- Q: What is the difference between CVE and CWE? A: CVE identifies specific known vulnerabilities in software products; CWE classifies the types of software weaknesses that cause vulnerabilities.
- Q: What does OWASP stand for? A: Open Worldwide Application Security Project (formerly Open Web Application Security Project).
- Q: Name the top 5 of the OWASP Top 10:2025 in order. A: (1) Broken Access Control, (2) Security Misconfiguration, (3) Cryptographic Failures, (4) Vulnerable Components, (5) Injection.
- Q: What is a zero-day vulnerability? A: A vulnerability with no available patch because the vendor is unaware of it or has not yet released a fix, giving them "zero days" to respond.
