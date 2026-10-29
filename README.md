<div align="center">

<img src="assets/banner.svg" width="100%" alt="Johnata Williamy — Cloud & DevSecOps Engineer"/>

<br/>

![Status](https://img.shields.io/badge/status-open__to__work-00FF41?style=flat-square&labelColor=000000)
![Local](https://img.shields.io/badge/local-Guarulhos%20%E2%80%93%20SP-00FF41?style=flat-square&labelColor=000000)
![Contrato](https://img.shields.io/badge/contrato-PJ%20%2F%20CLT-00FF41?style=flat-square&labelColor=000000)
![AWS](https://img.shields.io/badge/AWS%20CLF--C02-em%20prepara%C3%A7%C3%A3o-FF9900?style=flat-square&logo=amazon-aws&logoColor=white&labelColor=000000)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/SEU-USUARIO)
[![E-mail](https://img.shields.io/badge/E--mail-000000?style=for-the-badge&logo=gmail&logoColor=00FF41)](mailto:johnataichigo56@gmail.com)
[![Portfólio](https://img.shields.io/badge/Portf%C3%B3lio-000000?style=for-the-badge&logo=googlechrome&logoColor=00FF41)](https://johnataa.vercel.app)

<img src="assets/divider.svg" width="100%" alt=""/>

<img src="assets/terminal.svg" width="85%" alt="Terminal com resumo do perfil"/>

</div>

<img src="assets/divider.svg" width="100%" alt=""/>

## `root@kctxdev:~# cat /etc/sobre.conf`

```text
┌──(root㉿kctxdev)-[~]
└─# cat /etc/motd
   "Segurança não é um recurso. É a fundação."
   // mantenha o menor privilégio. assuma o vazamento. automatize a resposta.
```

Projeto e automatizo infraestrutura em nuvem em que **segurança, auditoria e custo são requisitos de arquitetura**, aplicando *Security by Design* e *Least Privilege* desde o primeiro commit.

```yaml
nome:        Johnata Williamy Sousa da Silva
cargo:       Analista Júnior em Cloud & DevSecOps
foco:        Cloud Security · IaC · CI/CD seguro · FinOps
formacao:    Cursando Segurança da Informação (Técnico/Superior)
idiomas:     Português (nativo) · Inglês (intermediário)
disponivel:  PJ / CLT em Cloud & Security
```

> **English:** Cloud & DevSecOps engineer focused on secure-by-default AWS infrastructure, event-driven incident response and least-privilege CI/CD pipelines.

<img src="assets/divider.svg" width="100%" alt=""/>

## `root@kctxdev:~# ./impacto --resumo`

```text
SEGURANÇA
  portas SSH expostas ........ 0      (acesso via SSM Session Manager)
  IPs públicos nas instâncias  0
  criptografia em repouso .... AES-256 (S3 e EBS) · IMDSv2 obrigatório

AUTOMAÇÃO
  deploys manuais ............ 0      (100% via GitHub Actions)
  credenciais no código ...... 0      (OIDC + Secrets Manager)
  ações automáticas/incidente  3      (isolar · coletar evidência · alertar)
  módulos Terraform .......... 6      (2 ambientes: dev e prod)

GOVERNANÇA
  auditoria de API ........... 100%   (CloudTrail multi-região)
  bloqueio de acesso público S3 100%
  alerta de custo ............ a partir de US$ 10
```

<img src="assets/divider.svg" width="100%" alt=""/>

## `root@kctxdev:~# ls -la ./projetos/`

### 🛰️ CloudGuard — Detecção, Resposta a Incidentes & FinOps
[Repositório](https://github.com/kctxdev/cloudguard-aws-security) · `Terraform` `GuardDuty` `EventBridge` `Lambda (Python)` `CloudTrail` `SNS` `SSM`

| | |
|---|---|
| **Problema** | Resposta manual a ameaças é lenta e inconsistente, e recursos ociosos geram custo silencioso. |
| **Solução** | Plataforma orientada a eventos que detecta, contém e remedia riscos de segurança e de custo automaticamente. |
| **Resultado** | Para ameaças de severidade ≥ 7: isola a instância, preserva o finding no S3 como evidência forense e alerta o time via SNS. Também remedia buckets S3 públicos, aplica tags de Centro de Custo e desliga recursos ociosos. |

<details>
<summary><b>Ver arquitetura</b></summary>

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor':'#06210E','primaryTextColor':'#00FF41','lineColor':'#22D3EE','primaryBorderColor':'#00FF41'}}}%%
flowchart LR
    A[Evento na conta AWS] --> B[CloudTrail / GuardDuty]
    B --> C[EventBridge<br/>severidade ≥ 7]
    C --> D[Lambda de resposta]
    D --> E[Instância isolada]
    D --> F[Evidência no S3]
    D --> G[Alerta via SNS]
    D --> H[S3 público → privado]
    D --> I[Tags de Centro de Custo]
    D --> J[Recurso ocioso desligado]
```

</details>

### 🔐 Pipeline CI/CD DevSecOps
[Repositório](https://github.com/kctxdev/aws-cicd-devsecops) · `GitHub Actions` `Terraform` `Secrets Manager` `IAM`

| | |
|---|---|
| **Problema** | Chaves estáticas em código ou em secrets de CI são um vetor recorrente de vazamento. |
| **Solução** | Esteira com IaC de menor privilégio, segredos no Secrets Manager (sa-east-1) e deploy automático a cada push. |
| **Resultado** | 0 credenciais no código, 0 deploys manuais e `terraform fmt` obrigatório para o pipeline concluir. |

### 🌐 AWS Secure VPC · 📊 AWS Monitoramento
[aws-secure-vpc-terraform](https://github.com/kctxdev/aws-secure-vpc-terraform) · [aws-monitoramento-terraform](https://github.com/kctxdev/aws-monitoramento-terraform)

- **Baseline de rede e storage:** VPC com sub-redes, route tables, Internet Gateway e Security Group restrito; S3 com AES-256, versionamento e bloqueio total de acesso público.
- **Auditoria e custo:** CloudTrail com 100% das chamadas de API registradas, bucket de logs com política restrita (só o CloudTrail grava) e alarme de billing em US$ 10 com e-mail via SNS.

### 🤖 Caçador de Vagas Pro · 🎙️ Finance AI Voice API
- [cacador-de-vagas-bot](https://github.com/kctxdev/cacador-de-vagas-bot) · `Python` `BeautifulSoup4` `SQLite`: agrega vagas de 5+ sites em paralelo, com filtro por título, geolocalização via IP e cache de 30 min para respostas instantâneas.
- **Finance AI Voice API** · `Java` `Spring Boot` `Spring AI`: orçamento financeiro por comando de voz, com transcrição, *Tool Calling* e resposta em áudio.

<!-- Descomente e coloque o link real do repositório:
[Finance AI Voice API](https://github.com/kctxdev/NOME-DO-REPO)
-->

<img src="assets/divider.svg" width="100%" alt=""/>

## `root@kctxdev:~# nmap -sV stack`

<div align="center">

<img src="assets/nmap.svg" width="90%" alt="Scan nmap das habilidades"/>

<br/>

| Categoria | Tecnologias |
|:---|:---|
| **Cloud** | ![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=FF9900) ![EC2](https://img.shields.io/badge/EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white) ![S3](https://img.shields.io/badge/S3-569A31?style=flat-square&logo=amazons3&logoColor=white) ![IAM](https://img.shields.io/badge/IAM-DD344C?style=flat-square&logo=amazoniam&logoColor=white) ![Route53](https://img.shields.io/badge/Route53-8C4FFF?style=flat-square&logo=amazonroute53&logoColor=white) |
| **Segurança** | ![GuardDuty](https://img.shields.io/badge/GuardDuty-D91E75?style=flat-square&logo=amazon-aws&logoColor=white) ![CloudTrail](https://img.shields.io/badge/CloudTrail-232F3E?style=flat-square&logo=amazon-aws&logoColor=22D3EE) ![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=flat-square&logo=amazoncloudwatch&logoColor=white) ![KMS](https://img.shields.io/badge/KMS-232F3E?style=flat-square&logo=amazon-aws&logoColor=FFD700) |
| **DevOps & IaC** | ![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![AWS CLI](https://img.shields.io/badge/AWS_CLI-232F3E?style=flat-square&logo=amazon-aws&logoColor=white) |
| **Linguagens** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white) |
| **Sistemas** | ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white) ![Amazon Linux](https://img.shields.io/badge/Amazon_Linux-FF9900?style=flat-square&logo=amazon-aws&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white) |

</div>

<img src="assets/divider.svg" width="100%" alt=""/>

## `root@kctxdev:~# tail -f /var/log/andamento.log`

| Objetivo | Status |
|---|---|
| AWS Certified Cloud Practitioner (CLF-C02) | 🟡 Em preparação |
| Terraform avançado (módulos) | 🟡 Em andamento |
| Kubernetes & Container Security | 🟡 Em andamento |
| Certificação em Segurança da Informação | 🟡 Em andamento |
| Java + Spring Boot com IA | 🟢 Explorando |

**Construindo agora:** automações de governança e FinOps na AWS e pipelines CI/CD seguros.

<img src="assets/divider.svg" width="100%" alt=""/>

## `root@kctxdev:~# git log --graph --all`

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=kctxdev&show_icons=true&hide_border=true&bg_color=000000&title_color=00FF41&icon_color=00FF41&text_color=C9D1D9&count_private=true" alt="Estatísticas GitHub"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=kctxdev&layout=compact&hide_border=true&bg_color=000000&title_color=00FF41&text_color=C9D1D9" alt="Linguagens mais usadas"/>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kctxdev/kctxdev/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kctxdev/kctxdev/output/github-contribution-grid-snake.svg" />
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/kctxdev/kctxdev/output/github-contribution-grid-snake-dark.svg" />
</picture>

<br/><br/>

<img src="assets/footer.svg" width="100%" alt="$ contact --open"/>

</div>

<!-- WhatsApp: descomente apenas se quiser expor seu número publicamente
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5511959445413)
-->
