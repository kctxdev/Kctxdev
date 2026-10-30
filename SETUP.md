# Como publicar (2 minutos)

1. No GitHub, crie um repositório **público** chamado exatamente `kctxdev` (mesmo nome do seu usuário).
2. Envie todo o conteúdo desta pasta (incluindo `.github/` e `assets/`) para a branch `main`.
3. Aba **Settings → Actions → General → Workflow permissions** → marque **Read and write permissions** → Save.
4. Aba **Actions → Generate Snake → Run workflow**. Ele gera o worm hacker (branch `output`) e atualiza o `assets/stats.svg`. Roda sozinho a cada 6 horas.
5. Edite o README e troque `SEU-USUARIO` pelo seu usuário do LinkedIn.
6. Opcional: descomente o link do Finance AI Voice API e o do WhatsApp no final do README.

```bash
git init -b main && git add . && git commit -m "feat: perfil hacker"
git remote add origin git@github.com:kctxdev/kctxdev.git
git push -u origin main
```

Dica: se os números de "impacto" não refletirem exatamente seus projetos, ajuste o bloco `./impacto --resumo`.

---

## Já tinha o repositório? Atualize o workflow pelo site

1. No repositório: `.github/workflows/snake.yml` → ícone de lápis (Edit).
2. Apague tudo, cole o conteúdo do `snake.yml` deste pacote e clique em **Commit changes**.
3. Aba **Actions → Generate Snake → Run workflow** e espere ficar verde (cerca de 1 minuto).
4. Se existir `.github/workflows/stats.yml` de versões anteriores, apague.
5. Ctrl+F5 no perfil (o GitHub guarda imagens em cache por alguns minutos).

Se o `stats.svg` ficar com `--`: rode `bash scripts/atualizar.sh` na sua máquina ou abra o log do passo "Gerar stats.svg" no Actions e me mande a linha `ERRO`.
