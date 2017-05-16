#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os

from gabbi import exception
from gabbi.handlers import base

from six import string_types
from urllib3.filepost import encode_multipart_formdata


class Multipart(base.ContentHandler):

    @staticmethod
    def accepts(content_type):
        content_type = content_type.split(';', 1)[0].strip()
        return content_type == 'multipart/form-data'

    @staticmethod
    def dumps(data, pretty=False, test=None):
        if not isinstance(data, dict):
            raise exception.GabbiFormatError(
                'multipart data must be provided as a dict')

        def process_field(field):
            """Read in <@ prefixed fields as (filename, filedata) tuples.
            urllib3 will guess the mimetype based on suffix else it will
            default to `application/octet-stream'.
            """
            if isinstance(field, string_types) and field.startswith('<@'):
                filename = os.path.join(test.test_directory,
                                        field.replace('<@', ''))
                # urllib3 only seems happy with (filename, filecontent)
                # tuples for these fields.
                return (filename, open(filename, 'rb').read())
            else:
                return field

        processed_data = {k: process_field(v) for k, v in data.items()}
        body, content_type = encode_multipart_formdata(processed_data)

        # Update the content type with the boundary.
        test.test_data['request_headers'].update({'content-type':
                                                  content_type})
        return body
