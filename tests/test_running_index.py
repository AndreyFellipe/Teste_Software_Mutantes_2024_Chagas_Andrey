import pytest
import pandas as pd
from running_calculator.core.running_index import RunningIndex


class TestRunningIndex:
    analyzer = RunningIndex()

    @pytest.mark.parametrize(
        "target, distance, index", [
            ("00:17:30", "5km", 58),
            ("00:45:44", "10km", 44)
        ]
    )
    def test_nearest(self, target, distance, index):
        assert self.analyzer.nearest(target, distance) == index

    def test_pd_option(self):
        # Verifica se a configuração do pandas para exibição de DataFrame está correta
        assert pd.get_option('display.expand_frame_repr') is False

    def test_paces_tab_initialization(self):
        # Verifica se paces_tab foi inicializado corretamente e não é None
        assert self.analyzer.paces_tab is not None
