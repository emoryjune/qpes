from typing import Sequence, Literal

import pandas as pd

from ampel.abstract.AbsTiedLightCurveT2Unit import AbsTiedLightCurveT2Unit
from ampel.struct.UnitResult import UnitResult
from ampel.types import UBson
from ampel.view.LightCurve import LightCurve
from ampel.view.T2DocView import T2DocView
from ampel.model.StateT2Dependency import StateT2Dependency


from timewise.process import keys


class T2FindQPEs(AbsTiedLightCurveT2Unit):
    t2_dependency: Sequence[StateT2Dependency[Literal["T2StackVisits"]]]

    def process(self, light_curve: LightCurve, t2_views: Sequence[T2DocView]) -> UBson | UnitResult:
        records = [r.body[0] for r in t2_views][0]
        stacked_lightcurve = pd.DataFrame.from_records(records)
        diff_series = stacked_lightcurve['w1meanflux'].diff() #difference between consecutive rows
        stacked_lightcurve['three_consecutive_increase_diff'] = (diff_series > 0) & (diff_series.shift(1) > 0) #check if bigger than previous which is bigger than one before that
        #print(stacked_lightcurve[['w1meanflux', 'three_consecutive_increase_diff']])