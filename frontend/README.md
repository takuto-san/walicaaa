### 補足

```
my-next-app/
├── app/
│   ├── layout.tsx       # ページ全体に共通するレイアウトを定義（例えば、header, footerなど）
│   └── page.tsx         # 「/」にアクセスしたときに表示される画面

├── public/              # 静的ファイル（画像など）
├── next.config.js       # Next.js の設定ファイル
├── package.json         # プロジェクト情報と依存関係
└── tsconfig.json        # TypeScript の設定ファイル
```

### 参考

Next.js公式ドキュメント
https://nextjs.org/docs/app/getting-started/installation

Next.jsベストプラクティス
https://zenn.dev/akfm/books/nextjs-basic-principle

