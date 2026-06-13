"""
Declarative pyedi Mapping Definition matching member_7.12 JSON Schema from EDI 834 Benefit Enrollment
"""

EDI_MEMBER = {
    "name": "Member 834 Enrollment Claims Schema Mapping",
    "mapping_type": "only_mapped",

    "expressions": {
        "TEMPLATE": "detail.unmapped",
        
        # Core mapped demographics from Member Name Loop (2100A) & Demographics (DMG)
        "UNIQUEPERSONKEY": "detail.member_loop.member_name_NM1.member_id",
        "BENEFICIARYID": "detail.member_loop.member_name_NM1.member_id",
        "MEDICAIDID": "detail.member_loop.member_name_NM1.member_id",
        "LASTNAME": "detail.member_loop.member_name_NM1.member_last_name",
        "FIRSTNAME": "detail.member_loop.member_name_NM1.member_first_name",
        "MIDDLEINITIAL": "detail.member_loop.member_name_NM1.member_middle_name",
        "DATEOFBIRTH": "detail.member_loop.member_demographics_DMG.patient_birth_date",
        "GENDER": "detail.member_loop.member_demographics_DMG.patient_gender_code",
        
        # Permanent Address Information (Mapped to Residence Address N3/N4)
        "PERMANENTADDRESSLINE1": "detail.member_loop.member_residence_address_N3.address_line_1",
        "PERMANENTADDRESSLINE2": "detail.member_loop.member_residence_address_N3.address_line_2",
        "PERMANENTCITY": "detail.member_loop.member_residence_city_state_zip_N4.city_name",
        "PERMANENTSTATE": "detail.member_loop.member_residence_city_state_zip_N4.state_code",
        "PERMANENTZIPCODE": "detail.member_loop.member_residence_city_state_zip_N4.zip_code",
        "PERMANENTCOUNTY": "detail.member_loop.member_residence_city_state_zip_N4.county_name",
        
        # Communication (Mapped to Member Contact PER segment)
        "TELEPHONENUMBER": "detail.member_loop.member_communications_PER.communication_number_04",
        "EMAIL": "detail.member_loop.member_communications_PER.communication_number_06",
        "FAX": "detail.member_loop.member_communications_PER.communication_number_08",
        
        # Mailing Address (Mapped to Mailing Address N3/N4 in Loop 2100C if present)
        "MAILINGADDRESSLINE1": "detail.member_loop.member_mailing_address_N3.address_line_1",
        "MAILINGADDRESSLINE2": "detail.member_loop.member_mailing_address_N3.address_line_2",
        "MAILINGCITY": "detail.member_loop.member_mailing_city_state_zip_N4.city_name",
        "MAILINGSTATE": "detail.member_loop.member_mailing_city_state_zip_N4.state_code",
        "MAILINGZIPCODE": "detail.member_loop.member_mailing_city_state_zip_N4.zip_code",
        "MAILINGCOUNTY": "detail.member_loop.member_mailing_city_state_zip_N4.county_name",
        
        # Caretaker Info (Mapped to Custodial Parent Loop 2100F if present)
        "CARETAKERFIRSTNAME": "detail.member_loop.custodial_parent_NM1.caretaker_first_name",
        "CARETAKERLASTNAME": "detail.member_loop.custodial_parent_NM1.caretaker_last_name",
        "CARETAKERMIDDLEINITIAL": "detail.member_loop.custodial_parent_NM1.caretaker_middle_name",
        
        # Demographics details
        "RACE": "detail.member_loop.member_demographics_DMG.race_or_ethnicity_code",
        "RACEDATASOURCE": "detail.member_loop.member_demographics_DMG.race_data_source",
        "ETHNICITY": "detail.member_loop.member_demographics_DMG.ethnicity_code",
        "ETHNICITYDATASOURCE": "detail.member_loop.member_demographics_DMG.ethnicity_data_source",
        
        # Languages (Mapped to Language Loop 2100G)
        "SPOKENLANGUAGE": "detail.member_loop.member_language_LUI.spoken_language",
        "SPOKENLANGUAGESOURCE": "detail.member_loop.member_language_LUI.spoken_language_source",
        "WRITTENLANGUAGE": "detail.member_loop.member_language_LUI.written_language",
        "WRITTENLANGUAGESOURCE": "detail.member_loop.member_language_LUI.written_language_source",
        "OTHERLANGUAGE": "detail.member_loop.member_language_LUI.other_language",
        "OTHERLANGUAGESOURCE": "detail.member_loop.member_language_LUI.other_language_source",
        
        # Identifiers & Attributes
        "USCITIZEN": "detail.member_loop.member_demographics_DMG.citizenship_status_code",
        "DECEASEDDATE": "detail.member_loop.member_demographics_DMG.deceased_date",
        "MASKEDMEMBERID": "detail.unmapped",
        "ENROLLEEEDUCATION": "detail.unmapped",
        "ENROLLEEEMPLOYMENT": "detail.member_loop.member_employment_details.employment_status_code",
        
        # Alternate Keys
        "ALTERNATEKEY1": "detail.unmapped",
        "ALTERNATEKEY2": "detail.unmapped",
        "ALTERNATEKEY3": "detail.unmapped",
        "ALTERNATEKEY4": "detail.unmapped",
        "ALTERNATEKEY5": "detail.unmapped",
        "ALTERNATEKEY6": "detail.unmapped",
        "ALTERNATEKEY7": "detail.unmapped",
        "ALTERNATEKEY8": "detail.unmapped",
        "ALTERNATEKEY9": "detail.unmapped",
        "ALTERNATEKEY10": "detail.unmapped"
    }
}