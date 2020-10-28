from transstat.dash_app import create_app
# from transstat.track import run_spotting
from transstat.data_sources.kstat import update_data
from transstat.data_sources.transphoto import get_records
# import transstat.db.mock

if __name__ == '__main__':
    update_data()
    # get_records()
    app = create_app()
    app.run_server(debug=True, port=8050, host="0.0.0.0")

