from flask import Flask, render_template
from google.oauth2 import service_account
from google.analytics.data_v1beta.types import DateRange, Metric, RunReportRequest
from google.analytics.data_v1beta import BetaAnalyticsDataClient

app = Flask(__name__)

def get_active_users():
    credentials = service_account.Credentials.from_service_account_info({
        # ここにサービスアカウントの情報を入れます
        '/Users/th_11/Documents//Users/th_11/Documents/healthy-matter-440011-a1-f877781b6246.json'
    })
    client = BetaAnalyticsDataClient(credentials=credentials)
    from google.analytics.data_v1beta.types import Entity
    request = RunReportRequest(
        entity=Entity(property_id='YOUR-GA4-PROPERTY-ID'),
        date_ranges=[DateRange(start_date='2020-01-01', end_date='today')],
        metrics=[Metric(name='activeUsers')]
    )

    response = client.run_report(request)
    return response.rows[0].metric_values[0].value

@app.route('/')
def home():
    active_users = get_active_users()
    return render_template('index.html', active_users=active_users)

if __name__ == '__main__':
    app.run(debug=True)
