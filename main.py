from demographic_data_analyzer import demographic_analysis

if __name__ == "__main__":
    result = demographic_analysis()
    for key, value in result.items():
        print(f"{key}: {value}")
