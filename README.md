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

</div>

<img src="assets/h-sobre.svg" width="100%" alt="cat /etc/sobre.conf"/>

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

<img src="assets/h-impacto.svg" width="100%" alt="./impacto --resumo"/>

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

<img src="assets/h-projetos.svg" width="100%" alt="ls -la ./projetos/"/>

```bash
for r in cloudguard-aws-security SentinelCloud aws-cicd-devsecops \
         aws-secure-vpc-terraform aws-monitoramento-terraform cacador-de-vagas-bot
do git clone https://github.com/kctxdev/$r; done
```

| | Repositório | O que faz | Stack |
|:-:|:--|:--|:--|
| 🛰️ | [**cloudguard-aws-security**](https://github.com/kctxdev/cloudguard-aws-security) | Detecta ameaça no GuardDuty e **isola a instância sozinho**, guardando a evidência no S3. | `Terraform` `Lambda` `EventBridge` |
| 🛡️ | [**SentinelCloud**](https://github.com/kctxdev/SentinelCloud) | Scanner **somente leitura** de contas AWS: acha S3 aberto, SSH exposto e IAM admin, e mostra a correção. | `Python` `boto3` `CLI` |
| 🔐 | [**aws-cicd-devsecops**](https://github.com/kctxdev/aws-cicd-devsecops) | Pipeline que cria um cofre no Secrets Manager a cada push, **sem nenhuma chave no código**. | `GitHub Actions` `Terraform` |
| 🌐 | [**aws-secure-vpc-terraform**](https://github.com/kctxdev/aws-secure-vpc-terraform) | Baseline de rede e storage: VPC, Security Group mínimo e S3 criptografado, sem acesso público. | `Terraform` `VPC` `S3` |
| 📊 | [**aws-monitoramento-terraform**](https://github.com/kctxdev/aws-monitoramento-terraform) | CloudTrail + alarme de custo (US$ 10) com alerta por e-mail. | `CloudTrail` `CloudWatch` `SNS` |
| 🤖 | [**cacador-de-vagas-bot**](https://github.com/kctxdev/cacador-de-vagas-bot) | Bot de Telegram que busca vagas em 5+ sites, com filtro por título e cache de 30 min. | `Python` `SQLite` |
| 🎙️ | **Finance AI Voice API** | Orçamento financeiro por comando de voz (transcrição, Tool Calling e resposta em áudio). | `Java` `Spring AI` |

<!-- Descomente e coloque o link real do repositório:
[Finance AI Voice API](https://github.com/kctxdev/NOME-DO-REPO)
-->

<details>
<summary><b>$ ./cloudguard --arquitetura</b></summary>

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor':'#06210E','primaryTextColor':'#00FF41','lineColor':'#22D3EE','primaryBorderColor':'#00FF41'}}}%%
flowchart LR
    A[Evento na conta AWS] --> B[CloudTrail / GuardDuty]
    B --> C[EventBridge<br/>severidade ≥ 7]
    C --> D[Lambda de resposta]
    D --> E[Instância isolada]
    D --> F[Evidência no S3]
    D --> G[Alerta via SNS]
```

</details>

<img src="assets/h-stack.svg" width="100%" alt="nmap -sV stack"/>

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

<img src="assets/h-andamento.svg" width="100%" alt="tail -f /var/log/andamento.log"/>

| Objetivo | Status |
|---|---|
| AWS Certified Cloud Practitioner (CLF-C02) | 🟡 Em preparação |
| Terraform avançado (módulos) | 🟡 Em andamento |
| Kubernetes & Container Security | 🟡 Em andamento |
| Certificação em Segurança da Informação | 🟡 Em andamento |
| SentinelCloud (scanner CSPM AWS) | 🟢 Publicado |
| Java + Spring Boot com IA | 🟢 Explorando |

**Construindo agora:** automações de governança e FinOps na AWS e pipelines CI/CD seguros.

<img src="assets/h-git.svg" width="100%" alt="git log --graph --all"/>

<div align="center">

<img src="assets/stats.svg" width="100%" alt="Estatísticas e linguagens do GitHub"/>

<br/>

<img src="assets/activity.svg" width="100%" alt="Matriz de contribuições do GitHub"/>

<br/><br/>

<img src="assets/footer.svg" width="100%" alt="$ contact --open"/>

</div>

<!-- WhatsApp: descomente apenas se quiser expor seu número publicamente
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5511959445413)
-->
