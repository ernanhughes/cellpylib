import unittest

import pytest
import numpy as np

import cellpylib as cpl


class TestApproximateEntropy(unittest.TestCase):

    def test_apen_string(self):
        self.assertAlmostEqual(cpl.apen('112012210'), 0.845297799381828)
        self.assertAlmostEqual(cpl.apen('200022211'), 0.6720110042418417)
        self.assertAlmostEqual(cpl.apen('210222001'), 0.845297799381828)
        self.assertAlmostEqual(cpl.apen('101211011'), 0.7108955985334597)
        self.assertAlmostEqual(cpl.apen('102012212'), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen('101221002'), 0.8075424578717401)
        self.assertAlmostEqual(cpl.apen('111002012'), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen('202122111'), 0.7679050283924354)
        self.assertAlmostEqual(cpl.apen('011101220'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('011220201'), 0.6342556627317537)
        self.assertAlmostEqual(cpl.apen('222100001'), 0.4333181911312869)
        self.assertAlmostEqual(cpl.apen('212112021'), 0.5292122152818808)
        self.assertAlmostEqual(cpl.apen('020210222'), 0.5572868307502927)
        self.assertAlmostEqual(cpl.apen('110201211'), 0.9111277563603284)
        self.assertAlmostEqual(cpl.apen('022220112'), 0.6724349432497736)
        self.assertAlmostEqual(cpl.apen('111101112'), 0.38980394055976986)
        self.assertAlmostEqual(cpl.apen('120211111'), 0.5376088033934733)
        self.assertAlmostEqual(cpl.apen('221022012'), 0.9111277563603284)
        self.assertAlmostEqual(cpl.apen('020220021'), 0.5292122152818806)
        self.assertAlmostEqual(cpl.apen('000022102'), 0.5572868307502927)
        self.assertAlmostEqual(cpl.apen('001120021'), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen('120020002'), 0.3840000356103066)
        self.assertAlmostEqual(cpl.apen('121111011'), 0.7025554552711372)
        self.assertAlmostEqual(cpl.apen('002222201'), 0.4494060535808746)
        self.assertAlmostEqual(cpl.apen('220200202'), 0.5685207485814306)
        self.assertAlmostEqual(cpl.apen('011021100'), 0.7679050283924354)
        self.assertAlmostEqual(cpl.apen('122100221'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('002110121'), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen('020000220'), 0.6843741748545092)
        self.assertAlmostEqual(cpl.apen('011221122'), 0.594618233252449)
        self.assertAlmostEqual(cpl.apen('022121011'), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen('100212002'), 0.6720110042418421)
        self.assertAlmostEqual(cpl.apen('111101211'), 0.7025554552711372)
        self.assertAlmostEqual(cpl.apen('002010020'), 0.7108955985334596)
        self.assertAlmostEqual(cpl.apen('200211210'), 0.8075424578717401)
        self.assertAlmostEqual(cpl.apen('221101201'), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen('000021121'), 0.4333181911312871)
        self.assertAlmostEqual(cpl.apen('002110011'), 0.7679050283924354)
        self.assertAlmostEqual(cpl.apen('021210020'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('011212010'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('112012201'), 0.49872420910185533)
        self.assertAlmostEqual(cpl.apen('121012110'), 0.5645541660803557)
        self.assertAlmostEqual(cpl.apen('220121021'), 0.8452977993818285)
        self.assertAlmostEqual(cpl.apen('202011012'), 0.6342556627317537)
        self.assertAlmostEqual(cpl.apen('002101201'), 0.8452977993818285)
        self.assertAlmostEqual(cpl.apen('220002100'), 0.7305736258902786)
        self.assertAlmostEqual(cpl.apen('210021021'), 0.22227605448121235)
        self.assertAlmostEqual(cpl.apen('122201001'), 0.6342556627317537)
        self.assertAlmostEqual(cpl.apen('012210220'), 0.8452977993818285)
        self.assertAlmostEqual(cpl.apen('201200120'), 0.260031395991301)
        self.assertAlmostEqual(cpl.apen('112102202'), 0.845297799381828)
        self.assertAlmostEqual(cpl.apen('221120022'), 0.9111277563603284)
        self.assertAlmostEqual(cpl.apen('021000021'), 0.3258613529698009)
        self.assertAlmostEqual(cpl.apen('100222220'), 0.4494060535808748)
        self.assertAlmostEqual(cpl.apen('021010121'), 0.49872420910185555)
        self.assertAlmostEqual(cpl.apen('221202222'), 0.7025554552711372)
        self.assertAlmostEqual(cpl.apen('221012222'), 0.5376088033934734)
        self.assertAlmostEqual(cpl.apen('000122100'), 0.6724349432497738)
        self.assertAlmostEqual(cpl.apen('011020211'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('220112002'), 0.845297799381828)
        self.assertAlmostEqual(cpl.apen('020002222'), 0.6339267665519992)
        self.assertAlmostEqual(cpl.apen('212210200'), 0.8452977993818285)
        self.assertAlmostEqual(cpl.apen('010120120'), 0.26003139599130076)
        self.assertAlmostEqual(cpl.apen('010101100'), 0.5685207485814302)
        self.assertAlmostEqual(cpl.apen('101101002'), 0.5292122152818806)
        self.assertAlmostEqual(cpl.apen('222111100'), 0.4333181911312869)
        self.assertAlmostEqual(cpl.apen('011121010'), 0.622692848720861)
        self.assertAlmostEqual(cpl.apen('100011011'), 0.6993327845225673)
        self.assertAlmostEqual(cpl.apen('020021100'), 0.737840961220342)
        self.assertAlmostEqual(cpl.apen('220100102'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('000110212'), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen('200101100'), 0.622692848720861)
        self.assertAlmostEqual(cpl.apen('102001022'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('111122121'), 0.6843741748545092)
        self.assertAlmostEqual(cpl.apen('101210102'), 0.4333181911312871)
        self.assertAlmostEqual(cpl.apen('110000022'), 0.39126737094036934)
        self.assertAlmostEqual(cpl.apen('211120210'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('012011200'), 0.49872420910185533)
        self.assertAlmostEqual(cpl.apen('221211112'), 0.6339267665519991)
        self.assertAlmostEqual(cpl.apen('101112110'), 0.6454895805628911)
        self.assertAlmostEqual(cpl.apen('110222121'), 0.7679050283924354)
        self.assertAlmostEqual(cpl.apen('010002011'), 0.7959796438608473)
        self.assertAlmostEqual(cpl.apen('200011102'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('121200001'), 0.4333181911312871)
        self.assertAlmostEqual(cpl.apen('110011121'), 0.818776375702878)
        self.assertAlmostEqual(cpl.apen('001201021'), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen('101222022'), 0.6724349432497736)
        self.assertAlmostEqual(cpl.apen('212101102'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('201220200'), 0.7024990104218669)
        self.assertAlmostEqual(cpl.apen('022100020'), 0.7959796438608473)
        self.assertAlmostEqual(cpl.apen('200112200'), 0.6720110042418417)
        self.assertAlmostEqual(cpl.apen('201211000'), 0.845297799381828)
        self.assertAlmostEqual(cpl.apen('000101202'), 0.737840961220342)
        self.assertAlmostEqual(cpl.apen('100211110'), 0.557286830750293)
        self.assertAlmostEqual(cpl.apen('122000022'), 0.5292122152818806)
        self.assertAlmostEqual(cpl.apen('102221002'), 0.49872420910185555)
        self.assertAlmostEqual(cpl.apen('202110020'), 0.6720110042418419)
        self.assertAlmostEqual(cpl.apen('002101202'), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen('120021201'), 0.6342556627317537)
        self.assertAlmostEqual(cpl.apen('010122022'), 0.6720110042418419)

    def test_apen_list(self):
        self.assertAlmostEqual(cpl.apen([1, 1, 2, 0, 1, 2, 2, 1, 0]), 0.845297799381828)
        self.assertAlmostEqual(cpl.apen([2, 0, 0, 0, 2, 2, 2, 1, 1]), 0.6720110042418417)
        self.assertAlmostEqual(cpl.apen([2, 1, 0, 2, 2, 2, 0, 0, 1]), 0.845297799381828)
        self.assertAlmostEqual(cpl.apen([1, 0, 1, 2, 1, 1, 0, 1, 1]), 0.7108955985334597)
        self.assertAlmostEqual(cpl.apen([1, 0, 2, 0, 1, 2, 2, 1, 2]), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen([1, 0, 1, 2, 2, 1, 0, 0, 2]), 0.8075424578717401)

    def test_apen_ndarray(self):
        self.assertAlmostEqual(cpl.apen(np.array([1, 1, 2, 0, 1, 2, 2, 1, 0])), 0.845297799381828)
        self.assertAlmostEqual(cpl.apen(np.array([2, 0, 0, 0, 2, 2, 2, 1, 1])), 0.6720110042418417)
        self.assertAlmostEqual(cpl.apen(np.array([2, 1, 0, 2, 2, 2, 0, 0, 1])), 0.845297799381828)
        self.assertAlmostEqual(cpl.apen(np.array([1, 0, 1, 2, 1, 1, 0, 1, 1])), 0.7108955985334597)
        self.assertAlmostEqual(cpl.apen(np.array([1, 0, 2, 0, 1, 2, 2, 1, 2])), 0.8452977993818283)
        self.assertAlmostEqual(cpl.apen(np.array([1, 0, 1, 2, 2, 1, 0, 0, 2])), 0.8075424578717401)

    def test_apen_unsupported_sequence_type(self):
        with pytest.raises(Exception) as e:
            cpl.apen({1, 2, 3})
        self.assertTrue("unsupported sequence type: <class 'set'>" in str(e.value))