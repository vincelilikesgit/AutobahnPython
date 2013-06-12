###############################################################################
##
##  Copyright 2013 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

__all__ = ["PerMessageCompressOffer",
           "PerMessageCompressOfferAccept",
           "PerMessageCompressResponse",
           "PerMessageCompressResponseAccept",
           "PerMessageCompress",

           "PerMessageDeflateOffer",
           "PerMessageDeflateOfferAccept",
           "PerMessageDeflateResponse",
           "PerMessageDeflateResponseAccept",
           "PerMessageDeflate",

           "PerMessageBzip2Offer",
           "PerMessageBzip2OfferAccept",
           "PerMessageBzip2Response",
           "PerMessageBzip2ResponseAccept",
           "PerMessageBzip2",

           "PERMESSAGE_COMPRESSION_EXTENSION"
           ]

from compress_base import *
from compress_deflate import *
from compress_bzip2 import *


## class for "permessage-deflate" and "permessage-bzip2" are always available
##
PERMESSAGE_COMPRESSION_EXTENSION = {

   PerMessageDeflateMixin.EXTENSION_NAME: {
      'Offer': PerMessageDeflateOffer,
      'OfferAccept': PerMessageDeflateOfferAccept,
      'Response': PerMessageDeflateResponse,
      'ResponseAccept': PerMessageDeflateResponseAccept,
      'PMCE': PerMessageDeflate},

   PerMessageBzip2Mixin.EXTENSION_NAME: {
      'Offer': PerMessageBzip2Offer,
      'OfferAccept': PerMessageBzip2OfferAccept,
      'Response': PerMessageBzip2Response,
      'ResponseAccept': PerMessageBzip2ResponseAccept,
      'PMCE': PerMessageBzip2}
}


## include "permessage-snappy" classes if Snappy is available
##
try:
   import snappy
   from compress_snappy import *
   PMCE = {
      'Offer': PerMessageSnappyOffer,
      'OfferAccept': PerMessageSnappyOfferAccept,
      'Response': PerMessageSnappyResponse,
      'ResponseAccept': PerMessageSnappyResponseAccept,
      'PMCE': PerMessageSnappy
   }
   PERMESSAGE_COMPRESSION_EXTENSION[PerMessageSnappyMixin.EXTENSION_NAME] = PMCE

   __all__.extend(["PerMessageSnappyOffer",
                   "PerMessageSnappyOfferAccept",
                   "PerMessageSnappyResponse",
                   "PerMessageSnappyResponseAccept",
                   "PerMessageSnappy"])

except ImportError:
   pass
