# Google Calendar Booking Bot

## How to run

1. Place your Google service account JSON as `service_account.json` in the root.
2. Install backend dependencies:
    ```
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
3. In another terminal, run the frontend:
    ```
    cd frontend
    streamlit run app.py
    ```
4. Open the Streamlit URL and chat!

## Notes

- No OAuth or Google account connection needed.
- When you book, you’ll receive a calendar invite by email.