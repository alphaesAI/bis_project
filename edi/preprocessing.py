import json
from preprocessing.parser import EDIParser
from preprocessing.formatter import TransactionFormatter
from preprocessing.mappings.csv_schema_mapper import CSVSchemaMapper
from preprocessing.mappings.csv_converter import CSVConverter


def main():
    """
    Main EDI processing pipeline:
    1. Parse raw EDI file
    2. Format to structured JSON
    3. Map to flat dictionary/dictionaries
    4. Convert to CSV
    
    Handles both single and multiple member records automatically.
    """
    
    # Configuration
    input_edi_path = "/Workspace/Users/logi@openhealthagents.org/edi/source/834member.txt"
    schema_dir = "/Workspace/Users/logi@openhealthagents.org/edi/datalake-dev/JSON/Schema"
    output_csv_path = "/Workspace/Users/logi@openhealthagents.org/edi/processed/member.csv"
    
    # Initialize components
    parser = EDIParser()
    formatter = TransactionFormatter()
    csv_mapper = CSVSchemaMapper()
    csv_converter = CSVConverter(schemas_dir=schema_dir)

    # Step 1: Parse raw EDI
    print("Parsing raw EDI file...")
    generic_json = parser.parse(input_edi_path)

    # Step 2: Format to structured JSON (returns dict or list of dicts)
    print("\nFormatting to structured JSON...")
    structured_json = formatter.format(generic_json)
    
    # Determine record count
    record_count = len(structured_json) if isinstance(structured_json, list) else 1
    print(f"\nFound {record_count} member record(s)")
    
    # Step 3: Map to flat dictionary/dictionaries (preserves structure)
    print("Mapping member profile(s)...")
    member_profiles = csv_mapper.map_member(structured_json)
    
    # Step 4: Convert to CSV (handles both single and multiple records)
    print("Converting to CSV...")
    csv_converter.convert_members(
        mapped_member=member_profiles,
        output_csv_path=output_csv_path,
        schema_filename="member_7.12_schema.json"
    )
    
    print(f"\nProcessing complete. Output: {output_csv_path}")
    print(f"Total records processed: {record_count}")
    
    # Display all mapped fields from first record
    print("\n" + "="*80)
    print("ALL MAPPED FIELDS - First Record")
    print("="*80)
    
    first_record = member_profiles[0] if isinstance(member_profiles, list) else member_profiles
    
    # Sort fields alphabetically for easier reading
    sorted_fields = sorted(first_record.keys())
    
    # Display each field with its value
    for field in sorted_fields:
        value = first_record.get(field)
        # Show "N/A" for None/empty values, otherwise show the actual value
        display_value = value if value not in [None, ""] else "N/A"
        print(f"  {field}: {display_value}")
    
    print("="*80)
    print(f"Total fields mapped: {len(sorted_fields)}")
    print("="*80)


if __name__ == "__main__":
    main()
