# -*- coding: utf-8 -*-
# Copyright 2017-2020 The pyXem developers
#
# This file is part of pyXem.
#
# pyXem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyXem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyXem.  If not, see <http://www.gnu.org/licenses/>.

import pytest
import numpy as np

from pyxem.signals.diffraction_variance2d import DiffractionVariance2D
from pyxem.signals.diffraction_variance2d import ImageVariance
from pyxem.signals.diffraction_variance1d import DiffractionVariance1D
from pyxem.signals.electron_diffraction2d import ElectronDiffraction2D


class TestDiffractionVariance:
    def test_get_diffraction_variance_signal(self, diffraction_pattern):
        difvar = DiffractionVariance2D(diffraction_pattern)
        assert isinstance(difvar, DiffractionVariance2D)

    def test_1d_azimuthal_integration(self):
        var = DiffractionVariance2D(data=np.ones((3, 3, 3, 3,)))
        var.unit = "2th_rad"
        integration = var.get_azimuthal_integral1d(npt_rad=10)
        assert isinstance(integration, DiffractionVariance1D)


class TestImageVariance:
    def test_get_image_variance_signal(self, diffraction_pattern):
        imvar = ImageVariance(diffraction_pattern)
        assert isinstance(imvar, ImageVariance)
