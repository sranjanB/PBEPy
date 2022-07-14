try:
    raise BaseException("Base Exception raised.")
except Exception as e:
    print(f"Error Details {e}")
