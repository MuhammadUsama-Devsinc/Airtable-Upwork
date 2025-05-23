# Airtable to S3 Pipeline

A Python-based pipeline for fetching data from Airtable, processing images, and uploading them to AWS S3.

## Project Structure

```
Airtable-Upwork/
├── config.env                 # Environment variables (gitignored)
├── pipeline.py               # Main orchestration script
├── image_utils.py            # Image processing and S3 uploads
├── data_utils.py             # Airtable data handling
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your credentials:
   ```
   AIRTABLE_API_KEY=your_airtable_key
   AIRTABLE_BASE_ID=your_base_id
   AWS_ACCESS_KEY_ID=your_aws_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret
   S3_BUCKET=your_bucket_name
   ```

## Usage

Run the main pipeline:
```bash
python pipeline.py
```

## Features

- Fetch records from Airtable
- Process and transform image data
- Upload processed images to S3
- Export metadata to CSV

## Dependencies

- Python 3.12+
- See `requirements.txt` for Python package dependencies
