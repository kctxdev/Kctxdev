<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=0:0F2027,50:203A43,100:2C5364&height=230&section=header&text=Johnata%20Williamy&fontSize=54&fontColor=ffffff&fontAlignY=42&desc=Cloud%20%26%20DevSecOps%20%C2%B7%20Security%20by%20Design&descSize=20&descColor=00D4FF&descAlignY=64" width="100%" alt="Johnata Williamy"/>

**Infraestrutura em nuvem segura, auditável e automatizada.**
AWS · Terraform · IAM · CI/CD · FinOps

<br/>

<img src="https://img.shields.io/badge/Dispon%C3%ADvel-PJ%20%2F%20CLT-00A86B?style=flat-square&labelColor=0D1117" alt="Disponível"/>
<img src="https://img.shields.io/badge/Guarulhos%20%7C%20SP-Brasil-6C5CE7?style=flat-square&labelColor=0D1117" alt="Localização"/>
<img src="https://img.shields.io/badge/Ingl%C3%AAs-Intermedi%C3%A1rio-00A3B8?style=flat-square&labelColor=0D1117" alt="Inglês"/>
<img src="https://img.shields.io/github/followers/kctxdev?label=Followers&style=flat-square&color=00D4FF&labelColor=0D1117" alt="Followers"/>

<br/>

[**Portfólio**](https://johnataa.vercel.app) &nbsp;·&nbsp; [**GitHub**](https://github.com/kctxdev) &nbsp;·&nbsp; [**E-mail**](mailto:johnataichigo56@gmail.com) &nbsp;·&nbsp; [**WhatsApp**](https://wa.me/5511959445413)

</div>

<br/>

## Sobre

Analista Júnior em **Cloud & DevSecOps**, estudante de Segurança da Informação, com foco em AWS.

Projeto e automatizo ambientes em nuvem partindo de três princípios: **segurança desde a concepção** (*Security by Design*), **menor privilégio** (*Least Privilege*) e **tudo como código**, versionado, revisável e reproduzível.

<br/>

## O que entrego

<table>
<tr>
<td width="50%" valign="top">

#### ☁️ Cloud & Infraestrutura como Código
VPC, EC2, S3, IAM e Route53 provisionados com Terraform: padronizado, versionado e repetível.

</td>
<td width="50%" valign="top">

#### 🛡️ Segurança & Governança
Auditoria com CloudTrail, detecção de ameaças com GuardDuty, criptografia com KMS e MFA.

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🔁 CI/CD Seguro
Pipelines com GitHub Actions, gestão de segredos e deploys sem credenciais expostas.

</td>
<td width="50%" valign="top">

#### 💰 FinOps
Monitoramento de custos, alertas proativos e desligamento automático de recursos ociosos.

</td>
</tr>
</table>

<br/>

## Projetos em destaque

<table>
<tr>
<td width="50%" valign="top">

### 🛰️ CloudGuard
**Detecção e resposta automática a incidentes na AWS.**

Reduz o tempo entre a ameaça e a contenção, sem depender de ação manual.

- Isola instâncias comprometidas (GuardDuty, severidade ≥ 7)
- Preserva evidências no S3 e alerta o time via SNS
- Corrige buckets S3 públicos automaticamente
- Garante tags de centro de custo
- Desliga recursos ociosos (FinOps)

`Terraform` `GuardDuty` `Lambda` `EventBridge` `CloudTrail` `SNS`

[Ver repositório →](https://github.com/kctxdev/cloudguard-aws-security)

</td>
<td width="50%" valign="top">

### 🔐 Pipeline CI/CD DevSecOps
**Deploy de infraestrutura sem chaves no código.**

Elimina o deploy manual e a exposição de credenciais.

- Segredos gerenciados no AWS Secrets Manager
- IaC seguindo o menor privilégio
- Validação e deploy automáticos a cada push

`GitHub Actions` `Terraform` `Secrets Manager` `IAM`

<br/>

[Ver repositório →](https://github.com/kctxdev/aws-cicd-devsecops)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌐 AWS Secure VPC
**Base de rede e armazenamento segura desde o primeiro deploy.**

Acaba com configuração manual inconsistente e risco de vazamento.

- Sub-redes e security groups padronizados
- S3 criptografado, versionado e sem acesso público

`Terraform` `VPC` `S3` `HCL`

[Ver repositório →](https://github.com/kctxdev/aws-secure-vpc-terraform)

</td>
<td width="50%" valign="top">

### 📊 AWS Monitoramento
**Auditoria contínua e controle de custos.**

Evita cobranças surpresa e deixa a conta pronta para auditorias.

- Registro de todas as chamadas de API
- Alerta por e-mail quando o gasto passa de US$ 10

`CloudTrail` `CloudWatch` `SNS` `S3` `Terraform`

[Ver repositório →](https://github.com/kctxdev/aws-monitoramento-terraform)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎙️ Finance AI Voice API
**Orçamento financeiro por comandos de voz.**

Une back-end Java e IA generativa em uma API conversacional.

- Transcrição e interpretação dos comandos por IA
- Tool Calling para executar ações no orçamento
- Resposta por síntese de voz

`Java` `Spring Boot` `Spring AI`

<!-- Descomente e coloque o link real do repositório:
[Ver repositório →](https://github.com/kctxdev/NOME-DO-REPO)
-->

</td>
<td width="50%" valign="top">

### 🤖 Caçador de Vagas Pro
**Bot de Telegram que agrega vagas de vários sites.**

Economiza horas de busca manual e entrega só o que é relevante.

- Filtro de precisão contra falsos positivos
- Cache SQLite de 30 min com resposta instantânea
- Geolocalização automática via IP

`Python` `SQLite` `BeautifulSoup4` `Telegram API`

[Ver repositório →](https://github.com/kctxdev/cacador-de-vagas-bot)

</td>
</tr>
</table>

<br/>

## Arquitetura do CloudGuard

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor':'#203A43','primaryTextColor':'#ffffff','lineColor':'#00D4FF','primaryBorderColor':'#00D4FF'}}}%%
flowchart LR
    A[Evento na conta AWS] --> B[CloudTrail / GuardDuty]
    B --> C[EventBridge]
    C --> D[Lambda de resposta]
    D --> E[Instância isolada<br/>+ evidência no S3]
    D --> F[Bucket público<br/>→ privado]
    D --> G[Tags de centro<br/>de custo aplicadas]
    D --> H[Recurso ocioso<br/>desligado]
    D --> I[Alerta via SNS]
```

<br/>

## Stack

<div align="center">

| | |
|:--|:--|
| **☁️ Cloud** | ![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=FF9900) ![EC2](https://img.shields.io/badge/EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white) ![S3](https://img.shields.io/badge/S3-569A31?style=flat-square&logo=amazons3&logoColor=white) ![IAM](https://img.shields.io/badge/IAM-DD344C?style=flat-square&logo=amazoniam&logoColor=white) ![VPC](https://img.shields.io/badge/VPC-232F3E?style=flat-square&logo=amazon-aws&logoColor=00D4FF) ![Route53](https://img.shields.io/badge/Route53-8C4FFF?style=flat-square&logo=amazonroute53&logoColor=white) |
| **🛡️ Segurança** | ![CloudTrail](https://img.shields.io/badge/CloudTrail-232F3E?style=flat-square&logo=amazon-aws&logoColor=00D4FF) ![CloudWatch](https://img.shields.io/badge/CloudWatch-FF4F8B?style=flat-square&logo=amazoncloudwatch&logoColor=white) ![GuardDuty](https://img.shields.io/badge/GuardDuty-D91E75?style=flat-square&logo=amazon-aws&logoColor=white) ![KMS](https://img.shields.io/badge/KMS-232F3E?style=flat-square&logo=amazon-aws&logoColor=FFD700) ![MFA](https://img.shields.io/badge/MFA-00A86B?style=flat-square&logo=letsencrypt&logoColor=white) |
| **⚙️ DevOps** | ![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![AWS CLI](https://img.shields.io/badge/AWS_CLI-232F3E?style=flat-square&logo=amazon-aws&logoColor=white) ![YAML](https://img.shields.io/badge/YAML-CB171E?style=flat-square&logo=yaml&logoColor=white) ![JSON](https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white) |
| **💻 Desenvolvimento** | ![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white) |
| **🖥️ Sistemas & Redes** | ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white) ![Amazon Linux](https://img.shields.io/badge/Amazon_Linux-FF9900?style=flat-square&logo=amazon-aws&logoColor=white) ![DNS](https://img.shields.io/badge/DNS%20%2F%20Networking-00A3B8?style=flat-square&logo=cisco&logoColor=white) |
| **🧰 Ferramentas** | ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white) ![Figma](https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=figma&logoColor=white) |

</div>

<br/>

## Em desenvolvimento

| Frente | Status |
|:--|:--|
| AWS Certified Cloud Practitioner (CLF-C02) | 🟡 Em preparação |
| Terraform avançado (modules) | 🟡 Em andamento |
| Kubernetes & Container Security | 🟡 Em andamento |
| Certificação em Segurança da Informação | 🟡 Em andamento |
| Automações de governança e FinOps na AWS | 🔵 Em construção |
| Java + Spring Boot com IA | 🔵 Em exploração |

<br/>

## GitHub

<div align="center">

<img height="150" src="https://github-readme-stats.vercel.app/api?username=kctxdev&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00D4FF&icon_color=6C5CE7&text_color=c9d1d9&count_private=true" alt="Estatísticas GitHub"/>
<img height="150" src="https://github-readme-stats.vercel.app/api/top-langs/?username=kctxdev&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00D4FF&text_color=c9d1d9" alt="Linguagens mais usadas"/>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kctxdev/kctxdev/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kctxdev/kctxdev/output/github-contribution-grid-snake.svg" />
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/kctxdev/kctxdev/output/github-contribution-grid-snake-dark.svg" />
</picture>

</div>

<br/>

## Contato

Aberto a oportunidades **PJ / CLT** em Cloud & Security.

<div align="center">

<!-- Descomente e troque pelo seu link real do LinkedIn:
<a href="https://www.linkedin.com/in/SEU-USUARIO"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
-->
<a href="mailto:johnataichigo56@gmail.com"><img src="https://img.shields.io/badge/E--mail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail"/></a>
<a href="https://wa.me/5511959445413"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>
<a href="https://johnataa.vercel.app"><img src="https://img.shields.io/badge/Portf%C3%B3lio-FF9900?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfólio"/></a>
<a href="https://github.com/kctxdev"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2C5364,50:203A43,100:0F2027&height=90&section=footer" width="100%" alt="footer"/>

</div>
