#comprehensive style for Dict
import pprint
from typing import Dict
data : Dict[str,str] ={"Name":"ali hamza",
                      "fname":"zakaullah",
                      "Education":"metric"}
pprint.pprint(data)
{v:k for k,v in data.items()}