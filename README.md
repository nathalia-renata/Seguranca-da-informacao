# 🛡️ Segurança da Informação e Cibersegurança

## 📝 Descrição

Este repositório reúne relatórios acadêmicos, análises teóricas e scripts práticos desenvolvidos em Python focados em **Segurança da Informação** e **Cibersegurança Defensiva/Ofensiva Ética**. O objetivo é documentar o funcionamento de algoritmos criptográficos, mapeamento de vulnerabilidades em redes, vetores de infecção por malwares e mitigações de falhas web.

## 🚀 Conteúdos e Tópicos Abordados

- **🔐 Criptografia e Integridade de Dados:**
  - **Funções de Hash:** Comparação entre algoritmos obsoletos (MD5) e modernos (SHA-256) para garantia de integridade[cite: 1].
  - **Criptografia Simétrica e Assimétrica:** Aplicação prática dos algoritmos AES (via biblioteca `cryptography`/Fernet) e RSA (2048 bits)[cite: 1].
  - **Proteção de Arquivos:** Script em Python demonstrando a cifragem de arquivos locais[cite: 1].

- **🔍 Reconhecimento e Gestão de Vulnerabilidades:**
  - **Análise de Risco:** Conceitos de vulnerabilidade, *exploit*, padronização **CVE** e pontuação de severidade **CVSS**[cite: 2].
  - **Análise de Serviços:** Riscos associados a serviços obsoletos/desatualizados como SSH 7.4, Apache 2.2 (sem TLS), SMBv1 (EternalBlue) e FTP anônimo[cite: 2].
  - **Port Scanner:** Script em Python utilizando a biblioteca `socket` para varredura e identificação de portas abertas na rede[cite: 2].

- **🦠 Análise de Ameaças (Spyware e Malware):**
  - **Keyloggers e Vetores de Infecção:** Estudo de caso sobre captação de dados, riscos e vetores comuns de contaminação[cite: 3].
  - **Demonstração Prática:** Implementação conceitual de monitoramento de eventos de teclado com a biblioteca `pynput`[cite: 3].

- **💉 Segurança Web & SQL Injection (SQLi):**
  - **Técnicas de Ataque:** Funcionamento de invasões do tipo *Login Bypass*, *UNION-based*, *Error-based* e *Blind SQLi*[cite: 3].
  - **Defesa e Mitigação:** Boas práticas de desenvolvimento seguro utilizando Consultas Parametrizadas (*Prepared Statements*), sanitização de dados e o Princípio do Mínimo Privilégio[cite: 3].

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.x
- **Bibliotecas:** `cryptography`, `pynput`, `socket`, `hashlib`[cite: 1, 2, 3]
- **Conceitos & Padrões:** Criptografia (AES/RSA), CVE, CVSS, SQL Injection, Prepared Statements[cite: 1, 2, 3]
- **Ferramentas:** VS Code, Git & GitHub
