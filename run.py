from src import service
if __name__ == "__main__":
    try:
        service.run(host='0.0.0.0', port=3007, debug=False)
    except Exception as e:
        print ('Service Not Responding')
