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


from gabbi import exception
from gabbi.handlers import base


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
        # TODO: insert actually dumping here
        # See http://stackoverflow.com/a/18888633/225997 for some
        # ideas. Besides that encoding,
        # test.test_data['request_headers']['content-type'] will
        # need to be cooked.
        # Expected input format something like (but we need to verify
        # this):
        # 
        # name: multipart test
        # POST: /somewhere
        # request_headers:
        #     content-type: multipart/form-data
        # data:
        #     alpha: 1
        #     beta: cow
        #     gamma: @<sample.png
        # status: 201
        #
        # An issue with this is that the content type of the file is
        # ambiguous. In the SO link above the mimetypes module is
        # used to do a best guess. This might be sufficient. If not
        # another option would be to optionally make the value of a
        # key be another dict like:
        # 
        # data:
        #     alpha: 1
        #     beta: cow
        #     gamma: @<sample.png
        #     delta:
        #          file: something
        #          type: image/jpeg
        #
