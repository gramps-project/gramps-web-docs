---
hide:
  - toc
---

# Gramps Web 開発: 概要

Gramps Web は、別々に開発された2つのコンポーネントからなるウェブアプリケーションです。

- **Gramps Web API** は、Pythonで書かれたRESTful APIで、Flaskに基づいています。ソースコードは [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/) にホストされています。データベースアクセスと系譜機能をGramps Pythonライブラリを直接活用して管理します。Gramps Webのバックエンドとして機能します。開発ドキュメントについては、[Backend](backend/index.md) を参照してください。
- **Gramps Web Frontend** は、Gramps Webのフロントエンドとして機能するJavascriptウェブアプリケーションです。ソースコードは [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/) にホストされています。開発ドキュメントについては、[Frontend](frontend/index.md) を参照してください。

バージョン管理についての注意: Gramps Web APIとGramps Webフロントエンドは独立してバージョン管理されています。現在、「Gramps Web」&ndash; 結合アプリケーション &ndash; には別のバージョン番号はありません。両プロジェクトは [SemVer](https://semver.org/) に従っています。

PythonやJavascriptの開発者でない場合でもGramps Webに貢献したい場合は、[Contribute](../contribute/contribute.md) をチェックしてください。
