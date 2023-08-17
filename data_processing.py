import boto3

def process_data(event, context):
    # Process data here (e.g., transformation, aggregation)
    processed_data = [item * 2 for item in event['data']]

    # Store processed data in S3
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='your-s3-bucket-name',
        Key='processed-data/output.json',
        Body=processed_data
    )

    return {
        'statusCode': 200,
        'body': 'Data processing and storage complete.'
    }

