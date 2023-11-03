import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_nollavaraston_nollalla_ja_pienemmällä(self):
        jekkuvarasto = Varasto(0.0)
        negatiivinenvarasto = Varasto(-1.0)

        self.assertAlmostEqual(jekkuvarasto.tilavuus, 0.0)
        self.assertAlmostEqual(negatiivinenvarasto.tilavuus, 0.0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_nolla_ja_negatiivinen_alku_saldo_muuttuu_nollaksi(self):
        jekkuvarasto = Varasto(0.0, 0.0)
        negatiivinenvarasto = Varasto(-1.0, -1.0)

        self.assertAlmostEqual(jekkuvarasto.saldo, 0.0)
        self.assertAlmostEqual(negatiivinenvarasto.saldo, 0.0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_negatiivisella_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-1.0)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_saldoa_jos_taytetaan_kokonaan(self):
        self.varasto.lisaa_varastoon(10)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_enemman_kuin_mahtuu_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_negatiivisella_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_liian_paljon_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_oikea_merkkijono(self):
        self.varasto.lisaa_varastoon(7.5)

        haluttu_merkkijono = "saldo = 7.5, vielä tilaa 2.5"


        self.assertEqual(str(self.varasto), haluttu_merkkijono)
