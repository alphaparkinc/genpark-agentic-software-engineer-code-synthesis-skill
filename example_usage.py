from client import AgenticSoftwareEngineerCodeSynthesisClient

def main():
    client = AgenticSoftwareEngineerCodeSynthesisClient()
    res = client.synthesize_application("Build real-time inventory monitoring dashboard", "React-Node")
    print(f"Generated Files: {res['generated_files_count']}")
    print(f"Test Coverage: {res['unit_test_coverage_pct']}%")

if __name__ == "__main__":
    main()
