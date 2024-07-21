#comprehensive style for Dict
import pprint
from typing import Dict
data : Dict[str,str] ={"Name":"ali hamza",
                      "fname":"zakaullah",}
{v:k for k,v in data.items()}