# Giro Gato Website — Flask + Google App Engine

Includes official Giro Gato artwork, `/`, `/privacy`, `/privacy-policy`, `/support`, `/health`, `robots.txt`, `sitemap.xml`.

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```
Visit http://localhost:8080.

## Deploy
1. Create a new GCP project and enable billing.
2. `gcloud config set project YOUR_PROJECT_ID`
3. `gcloud services enable appengine.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com`
4. `gcloud app create --region=us-central` (once per project; select a supported region).
5. `gcloud app deploy`
6. `gcloud app browse`
7. App Engine > Settings > Custom Domains: verify and map `girogato.com`; set DNS records exactly as Google provides.

## Before launch
- Replace the placeholder support email with a working mailbox using `SUPPORT_EMAIL` in app.yaml env_variables or code.
- Set `IOS_APP_URL` and `ANDROID_APP_URL` to official store listing links when available.
- **Review and customize the privacy policy** after auditing Firebase SDKs (Analytics, Crashlytics, Auth, etc.), advertising SDKs, consent, retention, children's audience, publisher identity, and actual data practices. The policy is provisional and must not be published as final without this review.
- Complete Apple App Privacy declarations consistent with the shipped app.
- If you enable website analytics, update the website privacy disclosure.

Example app.yaml config (add under the existing settings):
```yaml
env_variables:
  SUPPORT_EMAIL: "support@girogato.com"
  IOS_APP_URL: ""
  ANDROID_APP_URL: ""
```
