<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=200&section=header&text=Johnata%20Williamy&fontColor=00F0FF&fontSize=48&fontAlignY=38&desc=Cloud%20%26%20DevSecOps%20%7C%20AWS%20%7C%20Terraform&descAlignY=60&descSize=18" width="100%"/>

**Infraestrutura em nuvem segura, auditável e automatizada — *Security by Design*.**

<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=FF9900"/>
<img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/>

<img src="https://img.shields.io/badge/Guarulhos%20%7C%20SP-8A2BE2?style=flat-square&logo=googlemaps&logoColor=white"/>
<img src="https://img.shields.io/badge/Aberto%20a%20oportunidades-PJ%20%2F%20CLT-00C853?style=flat-square"/>

</div>

---

## 👋 Sobre mim

Sou **Analista Júnior em Cloud & DevSecOps**, com foco em **segurança da informação e AWS**. Meus projetos partem de um princípio simples: **segurança e governança não são uma etapa final — são parte do desenho da infraestrutura desde o primeiro commit.**

Trabalho com:

- **Infraestrutura como Código** (Terraform) para ambientes reproduzíveis e revisáveis
- **Menor Privilégio (Least Privilege)** em IAM, redes e segredos
- **Automação orientada a eventos** para detectar e corrigir riscos sem depender de ação manual
- **FinOps**: visibilidade e controle de custo como parte da governança

🎓 Cursando Segurança da Informação · 🗣️ Português (nativo) · Inglês (intermediário)

---

## 🎯 Cases de destaque

Cada projeto abaixo segue o formato **Problema → Solução → Impacto**.

### 🛰️ Cloud Guard — Governança Automática & FinOps
`AWS Lambda (Python)` `EventBridge` `CloudTrail` `Terraform`

| | |
|---|---|
| **Problema** | Buckets S3 públicos, recursos sem tag de centro de custo e instâncias ociosas geram risco de vazamento e desperdício, e dependem de alguém perceber e agir a tempo. |
| **Solução** | Plataforma orientada a eventos: o CloudTrail registra a ação, o EventBridge dispara e funções Lambda remediam automaticamente (bloqueio de acesso público, checagem de tags, desligamento de ociosos). Toda a infra provisionada com Terraform. |
| **Impacto** | Remediação em tempo quase real, em vez de depender de auditorias periódicas · Redução da janela de exposição de dados · Custos rastreáveis por centro de custo · Menos gasto com recursos esquecidos ligados. |

[![Ver repositório](https://img.shields.io/badge/Ver_repositório-00F0FF?style=for-the-badge&logo=github&logoColor=black)](https://github.com/kctxdev/cloudguard-aws-security)

---

### 🔐 Pipeline CI/CD DevSecOps
`GitHub Actions` `Terraform` `AWS Secrets Manager` `IAM`

| | |
|---|---|
| **Problema** | Chaves de acesso no código-fonte e deploys manuais são as causas mais comuns de incidentes em nuvem. |
| **Solução** | Esteira automatizada com segredos no AWS Secrets Manager, permissões IAM restritas ao necessário e deploy de infraestrutura via Terraform. |
| **Impacto** | Zero credenciais expostas no repositório · Deploys repetíveis e auditáveis · Superfície de ataque reduzida pelo menor privilégio. |

[![Ver repositório](https://img.shields.io/badge/Ver_repositório-8A2BE2?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kctxdev/aws-cicd-devsecops)

---

### 🌐 AWS Secure VPC (Terraform)
`Terraform` `VPC` `S3` `HCL`

| | |
|---|---|
| **Problema** | Redes criadas manualmente variam de ambiente para ambiente e acumulam configurações inseguras. |
| **Solução** | Módulo Terraform que provisiona VPC, sub-redes, security groups e bucket S3 seguro com padrões consistentes. |
| **Impacto** | Ambientes padronizados e criados em minutos · Segurança embutida no design, não adicionada depois · Base reutilizável para novos projetos. |

[![Ver repositório](https://img.shields.io/badge/Ver_repositório-00FF9C?style=for-the-badge&logo=github&logoColor=black)](https://github.com/kctxdev/aws-secure-vpc-terraform)

---

### 📊 AWS Monitoramento (Terraform)
`CloudTrail` `S3` `CloudWatch` `SNS` `Terraform`

| | |
|---|---|
| **Problema** | Sem trilha de auditoria e alertas de custo, incidentes e gastos inesperados só são percebidos tarde. |
| **Solução** | Auditoria contínua com CloudTrail armazenada em S3, métricas no CloudWatch e alertas via SNS, tudo como código. |
| **Impacto** | Rastreabilidade de ações na conta · Alertas proativos de custo e eventos · Base para conformidade e investigação de incidentes. |

[![Ver repositório](https://img.shields.io/badge/Ver_repositório-FF4F8B?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kctxdev/aws-monitoramento-terraform)

---

### 🤖 Caçador de Vagas Pro — Bot de Telegram
`Python` `pyTelegramBotAPI` `BeautifulSoup4` `SQLite3`

| | |
|---|---|
| **Problema** | Procurar vagas em vários sites é lento e cheio de resultados irrelevantes. |
| **Solução** | Bot que agrega vagas de múltiplos sites brasileiros, filtra falsos positivos ("Filtro Sniper"), usa cache SQLite de 30 min e detecta localização por IP. |
| **Impacto** | Respostas instantâneas via cache · Resultados mais relevantes por filtragem · Busca centralizada direto no Telegram. |

[![Ver repositório](https://img.shields.io/badge/Ver_repositório-26A5E4?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kctxdev/cacador-de-vagas-bot)

---

## 🧰 Stack técnica

| Área | Tecnologias |
|---|---|
| ☁️ **Cloud** | AWS (EC2, S3, IAM, VPC, Route 53, Lambda, EventBridge) |
| 🛡️ **Segurança & Governança** | CloudTrail, CloudWatch, KMS, GuardDuty, MFA, criptografia, Least Privilege |
| ⚙️ **DevOps & Automação** | Terraform, GitHub Actions, CI/CD, AWS CLI, Python, Bash |
| 🖥️ **Sistemas & Redes** | Linux (Ubuntu, Amazon Linux), DNS, redes, JSON/YAML |

---

## 📚 Em evolução

| Foco | Status |
|---|---|
| AWS Certified Cloud Practitioner (CLF-C02) | 🟢 Em fase final de preparação |
| Terraform avançado (módulos) | 🟡 Em andamento |
| Certificação em Segurança da Informação | 🟡 Em andamento |
| Kubernetes & Container Security | 🔵 Iniciando |

---

## 📈 GitHub

<div align="center">

<img height="165em" src="https://github-readme-stats.vercel.app/api?username=kctxdev&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00F0FF&icon_color=8A2BE2&text_color=c9d1d9&count_private=true"/>
<img height="165em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=kctxdev&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00F0FF&text_color=c9d1d9"/>

<img src="https://raw.githubusercontent.com/kctxdev/kctxdev/output/github-contribution-grid-snake-dark.svg"/>

</div>

---

## 📫 Contato

Disponível para oportunidades **PJ / CLT** em **Cloud, DevSecOps e Segurança**.

<div align="center">

<a href="https://www.linkedin.com/in/SEU-LINK-AQUI"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="mailto:johnataichigo56@gmail.com"><img src="https://img.shields.io/badge/E--mail-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://wa.me/5511959445413"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2C5364,50:203A43,100:0F2027&height=100&section=footer"/>

</div>
