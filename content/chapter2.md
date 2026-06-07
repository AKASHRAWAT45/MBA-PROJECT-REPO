# Chapter 2: Review of Literature

## 2.1 Introduction to the Literature Review

This study rests on a systematic literature review that connects the inquiry to prior theory and evidence while identifying unresolved questions the present work seeks to answer. The evidence base spans scholarly articles, reputable industry analyses, regulatory guidance, and monographs in operations management, information systems, and financial services. Selection criteria prioritized source authority, topical fit with banking operations, and timeliness, supplemented by seminal works whose conceptual influence persists.

Rather than tracing developments year by year, the review follows thematic lines. These encompass: the development of operations management in service industries; automation and robotic process automation within financial institutions; artificial intelligence use cases in banking; associated benefits and performance effects; implementation obstacles and risks; governance and ethical considerations; and emerging trajectories such as generative AI and hyperautomation.

## 2.2 Operations Management in Financial Services

According to Slack, Brandon-Jones, and Johnston (2022), operations management encompasses designing, running, and refining the systems through which value is created and delivered. Service settings introduce intangibility, simultaneity, variability, and perishability, each of which undermines straightforward standardization. Banking operations therefore require a dual focus on efficiency and tailoring, given wide variation across customer segments, product portfolios, and risk exposures.

Chopra and Meindl (2021) argue that competitive positioning in service supply chains hinges on process architecture, capacity decisions, and quality systems. For banks, the operative "supply chain" consists of data streams, payment infrastructure, credit workflows, and partner networks rather than tangible inventory. Constraints in loan underwriting or know-your-customer verification translate directly into revenue leakage and weaker customer outcomes. A recurring theme in the literature is that digitization absent process re-engineering produces modest gains—a finding that frames assessment of AI and automation programs.

Fitzsimmons and Fitzsimmons (2019) present service blueprinting as a method for mapping customer-facing touchpoints alongside internal operational steps. AI and automation deployments most often begin in back-office and support functions, although conversational AI increasingly places algorithmic interfaces at the customer boundary.

## 2.3 Automation and Robotic Process Automation in Banking

Willcocks, Lacity, and Craig (2015) introduced scholarly treatment of RPA as a low-footprint integration approach that replicates human actions within graphical user interfaces. Banking applications span account servicing, mortgage documentation, trade finance data capture, and regulatory reporting. Their analysis indicates that RPA yields the fastest return where processes follow clear rules, transaction volumes are substantial, and exceptions remain infrequent.

Deloitte's banking automation surveys (2023, 2024) indicate that most global banks operate active RPA initiatives, with a growing share advancing toward intelligent automation by pairing bots with machine learning for exception management. Reported gains frequently include 30–60 percent shorter processing times for selected workflows and stronger audit documentation. The same surveys caution against "bot sprawl"—fragmented deployments that inflate maintenance overhead and create fragility when source applications are updated.

Ivangrad and Jayaratne (2018) examine workflow automation within financial compliance, observing that uniform audit trails and predictable execution lower human error in anti-money laundering alert handling. Their conclusions resonate with operational risk research linking repeatable, supervised procedures to more robust control frameworks.

From an operations strategy standpoint, automation priorities should be set through tools such as effort-versus-impact matrices. Tasks that are highly manual, high-volume, and low in complexity offer immediate opportunities. Credit decisions demanding nuanced judgment are better suited to decision support than end-to-end automation.

## 2.4 Artificial Intelligence in Banking Operations

Davenport and Ronanki (2018) categorize business AI into robotics and cognitive automation, computer vision, machine learning, natural language processing, and deep learning. Banks most commonly apply supervised learning to fraud surveillance and credit decision assistance. NLP underpins chatbots, sentiment analysis of customer communications, and clause extraction from legal texts.

Bholat et al. (2015), writing from the Bank of England, address big data analytics for central banks and supervised firms, stressing that data infrastructure must precede AI payoff. Institutions with siloed data warehouses face difficulty training dependable models; those building consolidated data lakes and feature stores describe shorter deployment cycles.

Arner, Barberis, and Buckley (2020) study FinTech and RegTech convergence, contending that AI enhances compliance operations via continuous surveillance and pattern recognition that surpass rule-only systems. RegTech tools automate supervisory reporting and internal control testing—functions directly tied to operations management in heavily regulated settings.

Recent explainable AI (XAI) scholarship responds to supervisors' insistence on interpretability. Rudin (2019) favors models that are interpretable by design for high-stakes choices over post-hoc rationalizations of opaque systems. Operational staff need to grasp why an alert triggered or a lending recommendation appeared to respond appropriately and meet audit expectations.

## 2.5 Customer Service Automation and Conversational AI

Xu, Chen, and Wang (2020) survey chatbot uptake in financial services, concluding that task-focused bots perform well on balance lookups, branch information, and card blocking, whereas open-ended dialogue remains difficult. Acceptance rises when institutions disclose bot identity and enable smooth handoff to human representatives.

Operations leaders assess contact centers via average handling time, first contact resolution, service level agreements, and customer effort scores. AI-driven routing assigns inquiries to specialized agents or bots according to intent classification, enhancing capacity use. Scholars warn that aggressive automation lacking empathy can erode brand credibility, especially for vulnerable clients or intricate disputes.

## 2.6 Credit Operations and Intelligent Document Processing

Research on lending operations identifies document-heavy workflows as a principal cost center. Intelligent Document Processing (IDP) merges optical character recognition, NLP, and machine learning to sort loan files, pull income figures, and check compliance with policy criteria. McKinsey work on digital lending indicates that automation can shrink origination cycles from days to hours for standardized offerings, while non-standard cases still demand manual scrutiny.

Credit models drawing on alternative data and machine learning provoke fairness debates. Kleinberg et al. (2018) show that algorithmic lending can sharpen predictive accuracy yet reproduce historical bias when training samples reflect discriminatory practices. Operations and risk teams must jointly oversee model validation, adverse action communication, and recurring fairness audits.

## 2.7 Fraud Detection and Operational Risk

Phua et al. (2010) supply foundational coverage of fraud detection methods ranging from rule engines to neural networks. Operational fraud units confront alert fatigue—excessive false positives that exhaust investigators and slow response to authentic threats. Machine learning lowers false positive volumes by establishing baselines of normal activity, though fraudsters' adaptive tactics necessitate ongoing model updates.

Basel Committee on Banking Supervision operational risk frameworks classify technology breakdowns, process failures, and external shocks as capital-relevant events. AI adds model risk: inadequately controlled algorithms can magnify losses. Model risk management literature (SR 11-7 in US banking, SS3/18 in UK) underscores independent validation, thorough documentation, and board-level oversight—organizational requirements extending beyond technical implementation.

## 2.8 Benefits Documented in Prior Research

Cross-source synthesis reveals recurring categories of benefit:

**Efficiency and cost:** Lower manual workload, compressed cycle times, round-the-clock processing, and reduced unit cost per transaction or account.

**Quality and accuracy:** Diminished keystroke mistakes, uniform enforcement of business rules, and richer data completeness where validation is automated.

**Scalability:** Capacity to absorb demand surges—loan moratorium requests or stimulus payouts, for example—without linear staff expansion.

**Compliance and auditability:** Tamper-evident logs, standardized decision routes, and quicker evidence retrieval for regulators.

**Customer experience:** Quicker replies, proactive notifications, tailored recommendations, and less repetition of information across channels.

**Risk reduction:** Earlier fraud identification, stronger AML pattern recognition, and predictive upkeep of IT operations infrastructure.

Quantitative benchmarks differ by institution and process boundary, motivating this project's comparative case approach instead of dependence on a single sector-wide average.

## 2.9 Challenges and Barriers in Literature

Scholarly and practitioner accounts alike identify layered impediments:

**Legacy technology:** Core banking platforms built decades earlier often lack APIs and real-time data feeds, hindering integration with AI environments.

**Data quality and silos:** Fragmented customer records, mismatched identifiers, and departmental data ownership obstruct model development and automation dependability.

**Talent and culture:** Scarcity of staff blending banking expertise with data science capability; employee anxiety over displacement; pushback from middle managers whose routines are altered.

**Governance and accountability:** Ambiguous responsibility across IT, operations, risk, and compliance for AI results; misalignment with existing committee arrangements.

**Regulatory uncertainty:** Shifting expectations on algorithmic accountability, data localization, and consumer protection slow production rollout.

**Vendor dependency:** Proprietary models and cloud concentration raise exit-strategy and supervisory-access concerns for critical operations.

**Cybersecurity:** Broader attack surfaces via API linkages, third-party AI services, and synthetic identity fraud aimed at automated onboarding.

## 2.10 Hyperautomation and Generative AI

Gartner defines hyperautomation as coordinating RPA, AI, process mining, and low-code platforms into connected end-to-end workflows. In banking, process mining surfaces deviations between actual and designed workflows, informing automation sequencing. Generative AI scholarship (2023–2025) examines applications including code support for legacy migration, summarization of customer interaction histories for agents, and synthetic data for model testing. Critical work flags hallucination risk, confidentiality exposure when public models are used, and the necessity of human-in-the-loop review for customer-facing content.

## 2.11 Indian Banking Context in Literature

RBI discussion papers and reports on FinTech, digital lending, and cybersecurity situate the Indian environment. NITI Aayog's national AI strategy documents outline sectoral prospects including financial services. Indian banking scholarship in outlets such as IIMB Management Review analyzes digital transformation in public sector banks, citing organizational inertia and capital limitations as brakes on automation scale.

Research on the Jan Dhan, Aadhaar, and mobile penetration (JAM trinity) underscores operational scale—millions of small-balance accounts needing economical service—that automation can address. Industry commentary often contrasts tier-1 private banks with smaller regional institutions, a pattern that supports this project's comparative design.

## 2.12 Theoretical Framework Adopted

The project combines the **Technology-Organization-Environment (TOE)** framework (Tornatzky & Fleischer, 1990) with **Process Theory** from operations management. TOE interprets adoption through technological readiness (infrastructure, compatibility), organizational factors (leadership, skills, culture), and environmental pressures (competition, regulation, customer demand). Process theory holds that results hinge on how technology is embedded in workflow design, not on deployment alone.

Rogers (2003) innovation adoption theory further clarifies why uptake diverges across banks and business units. Early adopters trial AI in fraud and service channels; late-majority institutions more often automate first where compliance pressure is acute.

## 2.13 Research Gap

Although literature on FinTech disruption and AI in general is voluminous, fewer works unite **operations management metrics**—cycle time, defect rate, capacity utilization, cost per unit—with **multi-bank comparative analysis** in India under consultancy-ready recommendations. Industry reports frequently champion technology without elaborating change management or governance. This project addresses the shortfall by connecting literature-based constructs to structured case evidence and practitioner guidance suited to Adhiita Consultancy Services' client setting.

## 2.14 Summary of Literature Review

The literature affirms that AI and automation can deliver significant operational gains in banking, yet outcomes depend on process clarity, data readiness, governance, and human capability. RPA yields tactical improvements; AI supports strategic differentiation when governed responsibly. Obstacles are as much organizational and regulatory as technical. Later chapters apply these findings through specified research objectives, methodology, and empirical examination of banking practices and case results.
