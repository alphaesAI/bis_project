# pyrefly: ignore [missing-import]
import sys
import os
from typing import Union, List, Dict

# Add the edi directory to sys.path so 'preprocessing' package can be found
if '/Users/logi@openhealthagents.org/edi' not in sys.path:
    sys.path.insert(0, '/Workspace/Users/logi@openhealthagents.org/edi')

from pyedi import SchemaMapper
from preprocessing.mappings.member_maxfields import MEMBER_MAXFIELDS


class CSVSchemaMapper:
    """Maps EDI structured JSON to CSV-friendly flat dictionaries.
    
    Handles both single record (dict) and multiple records (list of dicts) from StructuredFormatter.
    """

    def __init__(self):
        # Single mapper instance for member data
        self.member_mapper = SchemaMapper(MEMBER_MAXFIELDS)
        
        # Claims mapping not implemented yet
        self.claims_mapper = None

    def map_member(self, structured_json: Union[Dict, List[Dict]]) -> Union[Dict, List[Dict]]:
        """Map subscriber details to member CSV keys.
        
        Args:
            structured_json: Either a single member dict or a list of member dicts
            
        Returns:
            Mapped data in the same structure as input (dict or list of dicts)
        """
        return self._map_records(structured_json, self.member_mapper)

    def map_claims(self, structured_json: Union[Dict, List[Dict]]) -> Union[Dict, List[Dict]]:
        """Map claim loops to flat professional claim CSV keys.
        
        Args:
            structured_json: Either a single claim dict or a list of claim dicts
            
        Returns:
            Mapped data in the same structure as input (dict or list of dicts)
        """
        if self.claims_mapper is None:
            raise NotImplementedError("Claims mapping is not yet implemented")
        
        return self._map_records(structured_json, self.claims_mapper)
    
    def _map_records(self, data: Union[Dict, List[Dict]], mapper: SchemaMapper) -> Union[Dict, List[Dict]]:
        """Helper method to map single or multiple records using the provided mapper.
        
        Args:
            data: Either a single record dict or a list of record dicts
            mapper: SchemaMapper instance to use for mapping
            
        Returns:
            Mapped data in the same structure as input (dict or list of dicts)
        """
        # Handle list of records
        if isinstance(data, list):
            return [mapper.map(record) for record in data]
        
        # Handle single record
        return mapper.map(data)
