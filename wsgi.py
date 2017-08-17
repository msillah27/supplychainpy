# Copyright (c) 2015-2016, The Authors and Contributors
# <see AUTHORS file>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the
# following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os

from supplychainpy._helpers._config_file_paths import ABS_FILE_PATH_APPLICATION_CONFIG
from supplychainpy._helpers._pickle_config import deserialise_config
from supplychainpy.reporting.app import create_app
from supplychainpy.reporting.extensions import db

config = deserialise_config(ABS_FILE_PATH_APPLICATION_CONFIG)
app = create_app()

if os.name in ['posix', 'mac']:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/reporting.db'.format(config.get('database_path'))
elif os.name == 'nt':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}\\reporting.db'.format(config.get('database_path'))
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    """Target this file for running application on a server using http server like Nginx and Gunicorn. """
    app.run()