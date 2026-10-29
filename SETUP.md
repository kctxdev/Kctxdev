# Como publicar (2 minutos)

1. No GitHub, crie um repositório **público** chamado exatamente `kctxdev` (mesmo nome do seu usuário).
2. Envie todo o conteúdo desta pasta (incluindo `.github/` e `assets/`) para a branch `main`.
3. Aba **Settings → Actions → General → Workflow permissions** → marque **Read and write permissions** → Save.
4. Aba **Actions → Atualizar stats → Run workflow**. Ele lê seus dados no GitHub e gera `assets/stats.svg` e `assets/activity.svg` (roda sozinho a cada 6 horas).
5. Edite o README e troque `SEU-USUARIO` pelo seu usuário do LinkedIn.
6. Opcional: descomente o link do Finance AI Voice API e o do WhatsApp no final do README.

```bash
git init -b main && git add . && git commit -m "feat: perfil hacker"
git remote add origin git@github.com:kctxdev/kctxdev.git
git push -u origin main
```

Dica: se os números de "impacto" não refletirem exatamente seus projetos, ajuste o bloco `./impacto --resumo`.
