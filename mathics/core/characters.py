# -*- coding: utf8 -*-

u"""
    Mathics: a general-purpose computer algebra system
    Copyright (C) 2011 Jan Pöschko

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation either version 3 of the License or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not see <http://www.gnu.org/licenses/>.
"""

# Character ranges of letters
letter_pattern = unicode(u'a-zA-Z\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u0103'
u'\u0106\u0107\u010c-\u010f\u0112-\u0115\u011a-\u012d\u0131\u0141'
u'\u0142\u0147\u0148\u0150-\u0153\u0158-\u0161\u0164\u0165'
u'\u016e-\u0171\u017d\u017e\u0391-\u03a1\u03a3-\u03a9\u03b1-\u03c9'
u'\u03d1\u03d2\u03d5\u03d6\u03da-\u03e1\u03f0\u03f1\u03f5\u210a-\u210c'
u'\u2110-\u2113\u211b\u211c\u2128\u212c\u212d\u212f-\u2131'
u'\u2133-\u2138\uf6b2-\uf6b5\uf6b7\uf6b9\uf6ba-\uf6bc\uf6be\uf6bf'
u'\uf6c1-\uf700\uf730\uf731\uf770\uf772\uf773\uf776\uf779\uf77a'
u'\uf77d-\uf780\uf782-\uf78b\uf78d-\uf78f\uf790\uf793-\uf79a'
u'\uf79c-\uf7a2\uf7a4-\uf7bd\uf800-\uf833\ufb01\ufb02')

#TODO: letter-like and operator patterns

# All supported longname characters
named_characters = {
    'AAcute' : u'\u00E1',
    'ABar' : u'\u0101',
    'ACup' : u'\u0103',
    'ADoubleDot' : u'\u00E4',
    'AE' : u'\u00E6',
    'AGrave' : u'\u00E0',
    'AHat' : u'\u00E2',
    'Aleph' : u'\u2135',
    'AliasDelimiter' : u'\uF764',
    'AliasIndicator' : u'\uF768',
    'AlignmentMarker' : u'\uF760',
    'Alpha' : u'\u03B1',
    'AltKey' : u'\uF7D1',
    'And' : u'\u2227',
    'Angle' : u'\u2220',
    'Angstrom' : u'\u212B',
    'ARing' : u'\u00E5',
    'AscendingEllipsis' : u'\u22F0',
    'ATilde' : u'\u00E3',
    'AutoLeftMatch' : u'\uF3A8',
    'AutoOperand' : u'\uF3AE',
    'AutoPlaceholder' : u'\uF3A4',
    'AutoRightMatch' : u'\uF3A9',
    'AutoSpace' : u'\uF3AD',
    'Backslash' : u'\u2216',
    'BeamedEighthNote' : u'\u266B',
    'BeamedSixteenthNote' : u'\u266C',
    'Because' : u'\u2235',
    'Bet' : u'\u2136',
    'Beta' : u'\u03B2',
    'BlackBishop' : u'\u265D',
    'BlackKing' : u'\u265A',
    'BlackKnight' : u'\u265E',
    'BlackPawn' : u'\u265F',
    'BlackQueen' : u'\u265B',
    'BlackRook' : u'\u265C',
    'Breve' : u'\u02D8',
    'Bullet' : u'\u2022',
    'CAcute' : u'\u0107',
    'CapitalAAcute' : u'\u00C1',
    'CapitalABar' : u'\u0100',
    'CapitalACup' : u'\u0102',
    'CapitalADoubleDot' : u'\u00C4',
    'CapitalAE' : u'\u00C6',
    'CapitalAGrave' : u'\u00C0',
    'CapitalAHat' : u'\u00C2',
    'CapitalAlpha' : u'\u0391',
    'CapitalARing' : u'\u00C5',
    'CapitalATilde' : u'\u00C3',
    'CapitalBeta' : u'\u0392',
    'CapitalCAcute' : u'\u0106',
    'CapitalCCedilla' : u'\u00C7',
    'CapitalCHacek' : u'\u010C',
    'CapitalChi' : u'\u03A7',
    'CapitalDelta' : u'\u0394',
    'CapitalDHacek' : u'\u010E',
    'CapitalDifferentialD' : u'\uF74B',
    'CapitalDigamma' : u'\u03DC',
    'CapitalEAcute' : u'\u00C9',
    'CapitalEBar' : u'\u0112',
    'CapitalECup' : u'\u0114',
    'CapitalEDoubleDot' : u'\u00CB',
    'CapitalEGrave' : u'\u00C8',
    'CapitalEHacek' : u'\u011A',
    'CapitalEHat' : u'\u00CA',
    'CapitalEpsilon' : u'\u0395',
    'CapitalEta' : u'\u0397',
    'CapitalEth' : u'\u00D0',
    'CapitalGamma' : u'\u0393',
    'CapitalIAcute' : u'\u00CD',
    'CapitalICup' : u'\u012C',
    'CapitalIDoubleDot' : u'\u00CF',
    'CapitalIGrave' : u'\u00CC',
    'CapitalIHat' : u'\u00CE',
    'CapitalIota' : u'\u0399',
    'CapitalKappa' : u'\u039A',
    'CapitalKoppa' : u'\u03DE',
    'CapitalLambda' : u'\u039B',
    'CapitalLSlash' : u'\u0141',
    'CapitalMu' : u'\u039C',
    'CapitalNHacek' : u'\u0147',
    'CapitalNTilde' : u'\u00D1',
    'CapitalNu' : u'\u039D',
    'CapitalOAcute' : u'\u00D3',
    'CapitalODoubleAcute' : u'\u0150',
    'CapitalODoubleDot' : u'\u00D6',
    'CapitalOE' : u'\u0152',
    'CapitalOGrave' : u'\u00D2',
    'CapitalOHat' : u'\u00D4',
    'CapitalOmega' : u'\u03A9',
    'CapitalOmicron' : u'\u039F',
    'CapitalOSlash' : u'\u00D8',
    'CapitalOTilde' : u'\u00D5',
    'CapitalPhi' : u'\u03A6',
    'CapitalPi' : u'\u03A0',
    'CapitalPsi' : u'\u03A8',
    'CapitalRHacek' : u'\u0158',
    'CapitalRho' : u'\u03A1',
    'CapitalSampi' : u'\u03E0',
    'CapitalSHacek' : u'\u0160',
    'CapitalSigma' : u'\u03A3',
    'CapitalStigma' : u'\u03DA',
    'CapitalTau' : u'\u03A4',
    'CapitalTHacek' : u'\u0164',
    'CapitalTheta' : u'\u0398',
    'CapitalThorn' : u'\u00DE',
    'CapitalUAcute' : u'\u00DA',
    'CapitalUDoubleAcute' : u'\u0170',
    'CapitalUDoubleDot' : u'\u00DC',
    'CapitalUGrave' : u'\u00D9',
    'CapitalUHat' : u'\u00DB',
    'CapitalUpsilon' : u'\u03A5',
    'CapitalURing' : u'\u016E',
    'CapitalXi' : u'\u039E',
    'CapitalYAcute' : u'\u00DD',
    'CapitalZeta' : u'\u0396',
    'CapitalZHacek' : u'\u017D',
    'Cap' : u'\u2322',
    'CCedilla' : u'\u00E7',
    'Cedilla' : u'\u00B8',
    'CenterDot' : u'\u00B7',
    'CenterEllipsis' : u'\u22EF',
    'Cent' : u'\u00A2',
    'CHacek' : u'\u010D',
    'Checkmark' : u'\u2713',
    'Chi' : u'\u03C7',
    'CircleDot' : u'\u2299',
    'CircleMinus' : u'\u2296',
    'CirclePlus' : u'\u2295',
    'CircleTimes' : u'\u2297',
    'ClockwiseContourIntegral' : u'\u2232',
    'CloseCurlyDoubleQuote' : u'\u201D',
    'CloseCurlyQuote' : u'\u2019',
    'CloverLeaf' : u'\u2318',
    'ClubSuit' : u'\u2663',
    'Colon' : u'\u2236',
    'CommandKey' : u'\uF76A',
    'Congruent' : u'\u2261',
    'Conjugate' : u'\uF3C8',
    'ConjugateTranspose' : u'\uF3C9',
    'ConstantC' : u'\uF7DA',
    'Continuation' : u'\uF3B1',
    'ContourIntegral' : u'\u222E',
    'ControlKey' : u'\uF763',
    'Coproduct' : u'\u2210',
    'Copyright' : u'\u00A9',
    'CounterClockwiseContourIntegral' : u'\u2233',
    'Cross' : u'\uF4A0',
    'CupCap' : u'\u224D',
    'Cup' : u'\u2323',
    'CurlyCapitalUpsilon' : u'\u03D2',
    'CurlyEpsilon' : u'\u03B5',
    'CurlyKappa' : u'\u03F0',
    'CurlyPhi' : u'\u03C6',
    'CurlyPi' : u'\u03D6',
    'CurlyRho' : u'\u03F1',
    'CurlyTheta' : u'\u03D1',
    'Currency' : u'\u00A4',
    'Dagger' : u'\u2020',
    'Dalet' : u'\u2138',
    'Dash' : u'\u2013',
    'Degree' : u'\u00B0',
    'DeleteKey' : u'\uF7D0',
    'Del' : u'\u2207',
    'Delta' : u'\u03B4',
    'DescendingEllipsis' : u'\u22F1',
    'DHacek' : u'\u010F',
    'Diameter' : u'\u2300',
    'Diamond' : u'\u22C4',
    'DiamondSuit' : u'\u2662',
    'DifferenceDelta' : u'\u2206',
    'DifferentialD' : u'\uF74C',
    'Digamma' : u'\u03DD',
    'DiscreteRatio' : u'\uF4A4',
    'DiscreteShift' : u'\uF4A3',
    'DiscretionaryHyphen' : u'\u00AD',
    'DiscretionaryLineSeparator' : u'\uF76E',
    'DiscretionaryParagraphSeparator' : u'\uF76F',
    'Divide' : u'\u00F7',
    'DotEqual' : u'\u2250',
    'DotlessI' : u'\u0131',
    'DotlessJ' : u'\uF700',
    'DottedSquare' : u'\uF751',
    'DoubleContourIntegral' : u'\u222F',
    'DoubleDagger' : u'\u2021',
    'DoubledGamma' : u'\uF74A',
    'DoubleDownArrow' : u'\u21D3',
    'DoubledPi' : u'\uF749',
    'DoubleLeftArrow' : u'\u21D0',
    'DoubleLeftRightArrow' : u'\u21D4',
    'DoubleLeftTee' : u'\u2AE4',
    'DoubleLongLeftArrow' : u'\u27F8',
    'DoubleLongLeftRightArrow' : u'\u27FA',
    'DoubleLongRightArrow' : u'\u27F9',
    'DoublePrime' : u'\u2033',
    'DoubleRightArrow' : u'\u21D2',
    'DoubleRightTee' : u'\u22A8',
    'DoubleStruckA' : u'\uF6E6',
    'DoubleStruckB' : u'\uF6E7',
    'DoubleStruckC' : u'\uF6E8',
    'DoubleStruckCapitalA' : u'\uF7A4',
    'DoubleStruckCapitalB' : u'\uF7A5',
    'DoubleStruckCapitalC' : u'\uF7A6',
    'DoubleStruckCapitalD' : u'\uF7A7',
    'DoubleStruckCapitalE' : u'\uF7A8',
    'DoubleStruckCapitalF' : u'\uF7A9',
    'DoubleStruckCapitalG' : u'\uF7AA',
    'DoubleStruckCapitalH' : u'\uF7AB',
    'DoubleStruckCapitalI' : u'\uF7AC',
    'DoubleStruckCapitalJ' : u'\uF7AD',
    'DoubleStruckCapitalK' : u'\uF7AE',
    'DoubleStruckCapitalL' : u'\uF7AF',
    'DoubleStruckCapitalM' : u'\uF7B0',
    'DoubleStruckCapitalN' : u'\uF7B1',
    'DoubleStruckCapitalO' : u'\uF7B2',
    'DoubleStruckCapitalP' : u'\uF7B3',
    'DoubleStruckCapitalQ' : u'\uF7B4',
    'DoubleStruckCapitalR' : u'\uF7B5',
    'DoubleStruckCapitalS' : u'\uF7B6',
    'DoubleStruckCapitalT' : u'\uF7B7',
    'DoubleStruckCapitalU' : u'\uF7B8',
    'DoubleStruckCapitalV' : u'\uF7B9',
    'DoubleStruckCapitalW' : u'\uF7BA',
    'DoubleStruckCapitalX' : u'\uF7BB',
    'DoubleStruckCapitalY' : u'\uF7BC',
    'DoubleStruckCapitalZ' : u'\uF7BD',
    'DoubleStruckD' : u'\uF6E9',
    'DoubleStruckE' : u'\uF6EA',
    'DoubleStruckEight' : u'\uF7E3',
    'DoubleStruckF' : u'\uF6EB',
    'DoubleStruckFive' : u'\uF7E0',
    'DoubleStruckFour' : u'\uF7DF',
    'DoubleStruckG' : u'\uF6EC',
    'DoubleStruckH' : u'\uF6ED',
    'DoubleStruckI' : u'\uF6EE',
    'DoubleStruckJ' : u'\uF6EF',
    'DoubleStruckK' : u'\uF6F0',
    'DoubleStruckL' : u'\uF6F1',
    'DoubleStruckM' : u'\uF6F2',
    'DoubleStruckN' : u'\uF6F3',
    'DoubleStruckNine' : u'\uF7E4',
    'DoubleStruckO' : u'\uF6F4',
    'DoubleStruckOne' : u'\uF7DC',
    'DoubleStruckP' : u'\uF6F5',
    'DoubleStruckQ' : u'\uF6F6',
    'DoubleStruckR' : u'\uF6F7',
    'DoubleStruckS' : u'\uF6F8',
    'DoubleStruckSeven' : u'\uF7E2',
    'DoubleStruckSix' : u'\uF7E1',
    'DoubleStruckT' : u'\uF6F9',
    'DoubleStruckThree' : u'\uF7DE',
    'DoubleStruckTwo' : u'\uF7DD',
    'DoubleStruckU' : u'\uF6FA',
    'DoubleStruckV' : u'\uF6FB',
    'DoubleStruckW' : u'\uF6FC',
    'DoubleStruckX' : u'\uF6FD',
    'DoubleStruckY' : u'\uF6FE',
    'DoubleStruckZ' : u'\uF6FF',
    'DoubleStruckZero' : u'\uF7DB',
    'DoubleUpArrow' : u'\u21D1',
    'DoubleUpDownArrow' : u'\u21D5',
    'DoubleVerticalBar' : u'\u2225',
    'DownArrowBar' : u'\u2913',
    'DownArrow' : u'\u2193',
    'DownArrowUpArrow' : u'\u21F5',
    'DownBreve' : u'\uF755',
    'DownExclamation' : u'\u00A1',
    'DownLeftRightVector' : u'\u2950',
    'DownLeftTeeVector' : u'\u295E',
    'DownLeftVector' : u'\u21BD',
    'DownLeftVectorBar' : u'\u2956',
    'DownPointer' : u'\u25BE',
    'DownQuestion' : u'\u00BF',
    'DownRightTeeVector' : u'\u295F',
    'DownRightVector' : u'\u21C1',
    'DownRightVectorBar' : u'\u2957',
    'DownTeeArrow' : u'\u21A7',
    'DownTee' : u'\u22A4',
    'EAcute' : u'\u00E9',
    'Earth' : u'\u2641',
    'EBar' : u'\u0113',
    'ECup' : u'\u0115',
    'EDoubleDot' : u'\u00EB',
    'EGrave' : u'\u00E8',
    'EHacek' : u'\u011B',
    'EHat' : u'\u00EA',
    'EighthNote' : u'\u266A',
    'Element' : u'\u2208',
    'Ellipsis' : u'\u2026',
    'EmptyCircle' : u'\u25CB',
    'EmptyDiamond' : u'\u25C7',
    'EmptyDownTriangle' : u'\u25BD',
    'EmptyRectangle' : u'\u25AF',
    'EmptySet' : u'\u2205',
    'EmptySmallCircle' : u'\u25E6',
    'EmptySmallSquare' : u'\u25FB',
    'EmptySquare' : u'\u25A1',
    'EmptyUpTriangle' : u'\u25B3',
    'EmptyVerySmallSquare' : u'\u25AB',
    'EnterKey' : u'\uF7D4',
    'EntityEnd' : u'\uF3B9',
    'EntityStart' : u'\uF3B8',
    'Epsilon' : u'\u03F5',
    'Equal' : u'\uF431',
    'EqualTilde' : u'\u2242',
    'Equilibrium' : u'\u21CC',
    'Equivalent' : u'\u29E6',
    'ErrorIndicator' : u'\uF767',
    'EscapeKey' : u'\uF769',
    'Eta' : u'\u03B7',
    'Eth' : u'\u00F0',
    'Euro' : u'\u20AC',
    'Exists' : u'\u2203',
    'ExponentialE' : u'\uF74D',
    'FiLigature' : u'\uFB01',
    'FilledCircle' : u'\u25CF',
    'FilledDiamond' : u'\u25C6',
    'FilledDownTriangle' : u'\u25BC',
    'FilledLeftTriangle' : u'\u25C0',
    'FilledRectangle' : u'\u25AE',
    'FilledRightTriangle' : u'\u25B6',
    'FilledSmallCircle' : u'\uF750',
    'FilledSmallSquare' : u'\u25FC',
    'FilledSquare' : u'\u25A0',
    'FilledUpTriangle' : u'\u25B2',
    'FilledVerySmallSquare' : u'\u25AA',
    'FinalSigma' : u'\u03C2',
    'FirstPage' : u'\uF7FA',
    'FivePointedStar' : u'\u2605',
    'Flat' : u'\u266D',
    'FlLigature' : u'\uFB02',
    'Florin' : u'\u0192',
    'ForAll' : u'\u2200',
    'FormalA' : u'\uF800',
    'FormalB' : u'\uF801',
    'FormalC' : u'\uF802',
    'FormalCapitalA' : u'\uF81A',
    'FormalCapitalB' : u'\uF81B',
    'FormalCapitalC' : u'\uF81C',
    'FormalCapitalD' : u'\uF81D',
    'FormalCapitalE' : u'\uF81E',
    'FormalCapitalF' : u'\uF81F',
    'FormalCapitalG' : u'\uF820',
    'FormalCapitalH' : u'\uF821',
    'FormalCapitalI' : u'\uF822',
    'FormalCapitalJ' : u'\uF823',
    'FormalCapitalK' : u'\uF824',
    'FormalCapitalL' : u'\uF825',
    'FormalCapitalM' : u'\uF826',
    'FormalCapitalN' : u'\uF827',
    'FormalCapitalO' : u'\uF828',
    'FormalCapitalP' : u'\uF829',
    'FormalCapitalQ' : u'\uF82A',
    'FormalCapitalR' : u'\uF82B',
    'FormalCapitalS' : u'\uF82C',
    'FormalCapitalT' : u'\uF82D',
    'FormalCapitalU' : u'\uF82E',
    'FormalCapitalV' : u'\uF82F',
    'FormalCapitalW' : u'\uF830',
    'FormalCapitalX' : u'\uF831',
    'FormalCapitalY' : u'\uF832',
    'FormalCapitalZ' : u'\uF833',
    'FormalD' : u'\uF803',
    'FormalE' : u'\uF804',
    'FormalF' : u'\uF805',
    'FormalG' : u'\uF806',
    'FormalH' : u'\uF807',
    'FormalI' : u'\uF808',
    'FormalJ' : u'\uF809',
    'FormalK' : u'\uF80A',
    'FormalL' : u'\uF80B',
    'FormalM' : u'\uF80C',
    'FormalN' : u'\uF80D',
    'FormalO' : u'\uF80E',
    'FormalP' : u'\uF80F',
    'FormalQ' : u'\uF810',
    'FormalR' : u'\uF811',
    'FormalS' : u'\uF812',
    'FormalT' : u'\uF813',
    'FormalU' : u'\uF814',
    'FormalV' : u'\uF815',
    'FormalW' : u'\uF816',
    'FormalX' : u'\uF817',
    'FormalY' : u'\uF818',
    'FormalZ' : u'\uF819',
    'FreakedSmiley' : u'\uF721',
    'Function' : u'\uF4A1',
    'Gamma' : u'\u03B3',
    'Gimel' : u'\u2137',
    'GothicA' : u'\uF6CC',
    'GothicB' : u'\uF6CD',
    'GothicC' : u'\uF6CE',
    'GothicCapitalA' : u'\uF78A',
    'GothicCapitalB' : u'\uF78B',
    'GothicCapitalC' : u'\u212D',
    'GothicCapitalD' : u'\uF78D',
    'GothicCapitalE' : u'\uF78E',
    'GothicCapitalF' : u'\uF78F',
    'GothicCapitalG' : u'\uF790',
    'GothicCapitalH' : u'\u210C',
    'GothicCapitalI' : u'\u2111',
    'GothicCapitalJ' : u'\uF793',
    'GothicCapitalK' : u'\uF794',
    'GothicCapitalL' : u'\uF795',
    'GothicCapitalM' : u'\uF796',
    'GothicCapitalN' : u'\uF797',
    'GothicCapitalO' : u'\uF798',
    'GothicCapitalP' : u'\uF799',
    'GothicCapitalQ' : u'\uF79A',
    'GothicCapitalR' : u'\u211C',
    'GothicCapitalS' : u'\uF79C',
    'GothicCapitalT' : u'\uF79D',
    'GothicCapitalU' : u'\uF79E',
    'GothicCapitalV' : u'\uF79F',
    'GothicCapitalW' : u'\uF7A0',
    'GothicCapitalX' : u'\uF7A1',
    'GothicCapitalY' : u'\uF7A2',
    'GothicCapitalZ' : u'\u2128',
    'GothicD' : u'\uF6CF',
    'GothicE' : u'\uF6D0',
    'GothicEight' : u'\uF7ED',
    'GothicF' : u'\uF6D1',
    'GothicFive' : u'\uF7EA',
    'GothicFour' : u'\uF7E9',
    'GothicG' : u'\uF6D2',
    'GothicH' : u'\uF6D3',
    'GothicI' : u'\uF6D4',
    'GothicJ' : u'\uF6D5',
    'GothicK' : u'\uF6D6',
    'GothicL' : u'\uF6D7',
    'GothicM' : u'\uF6D8',
    'GothicN' : u'\uF6D9',
    'GothicNine' : u'\uF7EF',
    'GothicO' : u'\uF6DA',
    'GothicOne' : u'\uF7E6',
    'GothicP' : u'\uF6DB',
    'GothicQ' : u'\uF6DC',
    'GothicR' : u'\uF6DD',
    'GothicS' : u'\uF6DE',
    'GothicSeven' : u'\uF7EC',
    'GothicSix' : u'\uF7EB',
    'GothicT' : u'\uF6DF',
    'GothicThree' : u'\uF7E8',
    'GothicTwo' : u'\uF7E7',
    'GothicU' : u'\uF6E0',
    'GothicV' : u'\uF6E1',
    'GothicW' : u'\uF6E2',
    'GothicX' : u'\uF6E3',
    'GothicY' : u'\uF6E4',
    'GothicZ' : u'\uF6E5',
    'GothicZero' : u'\uF7E5',
    'GrayCircle' : u'\uF753',
    'GraySquare' : u'\uF752',
    'GreaterEqualLess' : u'\u22DB',
    'GreaterEqual' : u'\u2265',
    'GreaterFullEqual' : u'\u2267',
    'GreaterGreater' : u'\u226B',
    'GreaterLess' : u'\u2277',
    'GreaterSlantEqual' : u'\u2A7E',
    'GreaterTilde' : u'\u2273',
    'Hacek' : u'\u02C7',
    'HappySmiley' : u'\u263A',
    'HBar' : u'\u210F',
    'HeartSuit' : u'\u2661',
    'HermitianConjugate' : u'\uF3CE',
    'HorizontalLine' : u'\u2500',
    'HumpDownHump' : u'\u224E',
    'HumpEqual' : u'\u224F',
    'Hyphen' : u'\u2010',
    'IAcute' : u'\u00ED',
    'ICup' : u'\u012D',
    'IDoubleDot' : u'\u00EF',
    'IGrave' : u'\u00EC',
    'IHat' : u'\u00EE',
    'ImaginaryI' : u'\uF74E',
    'ImaginaryJ' : u'\uF74F',
    'ImplicitPlus' : u'\uF39E',
    'Implies' : u'\uF523',
    'Infinity' : u'\u221E',
    'Integral' : u'\u222B',
    'Intersection' : u'\u22C2',
    'InvisibleApplication' : u'\uF76D',
    'InvisibleComma' : u'\uF765',
    'InvisiblePostfixScriptBase' : u'\uF3B4',
    'InvisiblePrefixScriptBase' : u'\uF3B3',
    'InvisibleSpace' : u'\uF360',
    'InvisibleTimes' : u'\u2062',
    'Iota' : u'\u03B9',
    'Jupiter' : u'\u2643',
    'Kappa' : u'\u03BA',
    'KernelIcon' : u'\uF756',
    'Koppa' : u'\u03DF',
    'Lambda' : u'\u03BB',
    'LastPage' : u'\uF7FB',
    'LeftAngleBracket' : u'\u2329',
    'LeftArrowBar' : u'\u21E4',
    'LeftArrow' : u'\u2190',
    'LeftArrowRightArrow' : u'\u21C6',
    'LeftBracketingBar' : u'\uF603',
    'LeftCeiling' : u'\u2308',
    'LeftDoubleBracket' : u'\u301A',
    'LeftDoubleBracketingBar' : u'\uF605',
    'LeftDownTeeVector' : u'\u2961',
    'LeftDownVectorBar' : u'\u2959',
    'LeftDownVector' : u'\u21C3',
    'LeftFloor' : u'\u230A',
    'LeftGuillemet' : u'\u00AB',
    'LeftModified' : u'\uF76B',
    'LeftPointer' : u'\u25C2',
    'LeftRightArrow' : u'\u2194',
    'LeftRightVector' : u'\u294E',
    'LeftSkeleton' : u'\uF761',
    'LeftTee' : u'\u22A3',
    'LeftTeeArrow' : u'\u21A4',
    'LeftTeeVector' : u'\u295A',
    'LeftTriangle' : u'\u22B2',
    'LeftTriangleBar' : u'\u29CF',
    'LeftTriangleEqual' : u'\u22B4',
    'LeftUpDownVector' : u'\u2951',
    'LeftUpTeeVector' : u'\u2960',
    'LeftUpVector' : u'\u21BF',
    'LeftUpVectorBar' : u'\u2958',
    'LeftVector' : u'\u21BC',
    'LeftVectorBar' : u'\u2952',
    'LessEqual' : u'\u2264',
    'LessEqualGreater' : u'\u22DA',
    'LessFullEqual' : u'\u2266',
    'LessGreater' : u'\u2276',
    'LessLess' : u'\u226A',
    'LessSlantEqual' : u'\u2A7D',
    'LessTilde' : u'\u2272',
    'LetterSpace' : u'\uF754',
    'LightBulb' : u'\uF723',
    'LongDash' : u'\u2014',
    'LongEqual' : u'\uF7D9',
    'LongLeftArrow' : u'\u27F5',
    'LongLeftRightArrow' : u'\u27F7',
    'LongRightArrow' : u'\u27F6',
    'LowerLeftArrow' : u'\u2199',
    'LowerRightArrow' : u'\u2198',
    'LSlash' : u'\u0142',
    'Mars' : u'\u2642',
    'MathematicaIcon' : u'\uF757',
    'MeasuredAngle' : u'\u2221',
    'MediumSpace' : u'\u205F',
    'Mercury' : u'\u263F',
    'Mho' : u'\u2127',
    'Micro' : u'\u00B5',
    'MinusPlus' : u'\u2213',
    'Mu' : u'\u03BC',
    'Nand' : u'\u22BC',
    'Natural' : u'\u266E',
    'NegativeMediumSpace' : u'\uF383',
    'NegativeThickSpace' : u'\uF384',
    'NegativeThinSpace' : u'\uF382',
    'NegativeVeryThinSpace' : u'\uF380',
    'Neptune' : u'\u2646',
    'NestedGreaterGreater' : u'\u2AA2',
    'NestedLessLess' : u'\u2AA1',
    'NeutralSmiley' : u'\uF722',
    'NHacek' : u'\u0148',
    'NoBreak' : u'\u2060',
    'NonBreakingSpace' : u'\u00A0',
    'Nor' : u'\u22BD',
    'NotCongruent' : u'\u2262',
    'NotCupCap' : u'\u226D',
    'NotDoubleVerticalBar' : u'\u2226',
    'NotElement' : u'\u2209',
    'NotEqual' : u'\u2260',
    'NotEqualTilde' : u'\uF400',
    'NotExists' : u'\u2204',
    'NotGreater' : u'\u226F',
    'NotGreaterEqual' : u'\u2271',
    'NotGreaterFullEqual' : u'\u2269',
    'NotGreaterGreater' : u'\uF427',
    'NotGreaterLess' : u'\u2279',
    'NotGreaterSlantEqual' : u'\uF429',
    'NotGreaterTilde' : u'\u2275',
    'NotHumpDownHump' : u'\uF402',
    'NotHumpEqual' : u'\uF401',
    'NotLeftTriangle' : u'\u22EA',
    'NotLeftTriangleBar' : u'\uF412',
    'NotLeftTriangleEqual' : u'\u22EC',
    'NotLessEqual' : u'\u2270',
    'NotLessFullEqual' : u'\u2268',
    'NotLessGreater' : u'\u2278',
    'NotLess' : u'\u226E',
    'NotLessLess' : u'\uF422',
    'NotLessSlantEqual' : u'\uF424',
    'NotLessTilde' : u'\u2274',
    'Not' : u'\u00AC',
    'NotNestedGreaterGreater' : u'\uF428',
    'NotNestedLessLess' : u'\uF423',
    'NotPrecedes' : u'\u2280',
    'NotPrecedesEqual' : u'\uF42B',
    'NotPrecedesSlantEqual' : u'\u22E0',
    'NotPrecedesTilde' : u'\u22E8',
    'NotReverseElement' : u'\u220C',
    'NotRightTriangle' : u'\u22EB',
    'NotRightTriangleBar' : u'\uF413',
    'NotRightTriangleEqual' : u'\u22ED',
    'NotSquareSubset' : u'\uF42E',
    'NotSquareSubsetEqual' : u'\u22E2',
    'NotSquareSuperset' : u'\uF42F',
    'NotSquareSupersetEqual' : u'\u22E3',
    'NotSubset' : u'\u2284',
    'NotSubsetEqual' : u'\u2288',
    'NotSucceeds' : u'\u2281',
    'NotSucceedsEqual' : u'\uF42D',
    'NotSucceedsSlantEqual' : u'\u22E1',
    'NotSucceedsTilde' : u'\u22E9',
    'NotSuperset' : u'\u2285',
    'NotSupersetEqual' : u'\u2289',
    'NotTilde' : u'\u2241',
    'NotTildeEqual' : u'\u2244',
    'NotTildeFullEqual' : u'\u2247',
    'NotTildeTilde' : u'\u2249',
    'NotVerticalBar' : u'\u2224',
    'NTilde' : u'\u00F1',
    'Nu' : u'\u03BD',
    'Null' : u'\uF3A0',
    'NumberSign' : u'\uF724',
    'OAcute' : u'\u00F3',
    'ODoubleAcute' : u'\u0151',
    'ODoubleDot' : u'\u00F6',
    'OE' : u'\u0153',
    'OGrave' : u'\u00F2',
    'OHat' : u'\u00F4',
    'Omega' : u'\u03C9',
    'Omicron' : u'\u03BF',
    'OpenCurlyDoubleQuote' : u'\u201C',
    'OpenCurlyQuote' : u'\u2018',
    'OptionKey' : u'\uF7D2',
    'Or' : u'\u2228',
    'OSlash' : u'\u00F8',
    'OTilde' : u'\u00F5',
    'OverBrace' : u'\uFE37',
    'OverBracket' : u'\u23B4',
    'OverParenthesis' : u'\uFE35',
    'Paragraph' : u'\u00B6',
    'PartialD' : u'\u2202',
    'Phi' : u'\u03D5',
    'Pi' : u'\u03C0',
    'Piecewise' : u'\uF361',
    'Placeholder' : u'\uF528',
    'PlusMinus' : u'\u00B1',
    'Pluto' : u'\u2647',
    'Precedes' : u'\u227A',
    'PrecedesEqual' : u'\u2AAF',
    'PrecedesSlantEqual' : u'\u227C',
    'PrecedesTilde' : u'\u227E',
    'Prime' : u'\u2032',
    'Product' : u'\u220F',
    'Proportion' : u'\u2237',
    'Proportional' : u'\u221D',
    'Psi' : u'\u03C8',
    'QuarterNote' : u'\u2669',
    'RawAmpersand' : u'\u0026',
    'RawAt' : u'\u0040',
    'RawBackquote' : u'\u0060',
    'RawBackslash' : u'\u005C',
    'RawColon' : u'\u003A',
    'RawComma' : u'\u002C',
    'RawDash' : u'\u002D',
    'RawDollar' : u'\u0024',
    'RawDot' : u'\u002E',
    'RawDoubleQuote' : u'\u0022',
    'RawEqual' : u'\u003D',
    'RawEscape' : u'\u001B',
    'RawExclamation' : u'\u0021',
    'RawGreater' : u'\u003E',
    'RawLeftBrace' : u'\u007B',
    'RawLeftBracket' : u'\u005B',
    'RawLeftParenthesis' : u'\u0028',
    'RawLess' : u'\u003C',
    'RawNumberSign' : u'\u0023',
    'RawPercent' : u'\u0025',
    'RawPlus' : u'\u002B',
    'RawQuestion' : u'\u003F',
    'RawQuote' : u'\u0027',
    'RawRightBrace' : u'\u007D',
    'RawRightBracket' : u'\u005D',
    'RawRightParenthesis' : u'\u0029',
    'RawSemicolon' : u'\u003B',
    'RawSlash' : u'\u002F',
    'RawSpace' : u'\u0020',
    'RawStar' : u'\u002A',
    'RawTab' : u'\u0009',
    'RawTilde' : u'\u007E',
    'RawUnderscore' : u'\u005F',
    'RawVerticalBar' : u'\u007C',
    'RawWedge' : u'\u005E',
    'RegisteredTrademark' : u'\u00AE',
    'ReturnIndicator' : u'\u21B5',
    'ReturnKey' : u'\uF766',
    'ReverseDoublePrime' : u'\u2036',
    'ReverseElement' : u'\u220B',
    'ReverseEquilibrium' : u'\u21CB',
    'ReversePrime' : u'\u2035',
    'ReverseUpEquilibrium' : u'\u296F',
    'RHacek' : u'\u0159',
    'Rho' : u'\u03C1',
    'RightAngle' : u'\u221F',
    'RightAngleBracket' : u'\u232A',
    'RightArrow' : u'\u2192',
    'RightArrowBar' : u'\u21E5',
    'RightArrowLeftArrow' : u'\u21C4',
    'RightBracketingBar' : u'\uF604',
    'RightCeiling' : u'\u2309',
    'RightDoubleBracket' : u'\u301B',
    'RightDoubleBracketingBar' : u'\uF606',
    'RightDownTeeVector' : u'\u295D',
    'RightDownVector' : u'\u21C2',
    'RightDownVectorBar' : u'\u2955',
    'RightFloor' : u'\u230B',
    'RightGuillemet' : u'\u00BB',
    'RightModified' : u'\uF76C',
    'RightPointer' : u'\u25B8',
    'RightSkeleton' : u'\uF762',
    'RightTee' : u'\u22A2',
    'RightTeeArrow' : u'\u21A6',
    'RightTeeVector' : u'\u295B',
    'RightTriangle' : u'\u22B3',
    'RightTriangleBar' : u'\u29D0',
    'RightTriangleEqual' : u'\u22B5',
    'RightUpDownVector' : u'\u294F',
    'RightUpTeeVector' : u'\u295C',
    'RightUpVector' : u'\u21BE',
    'RightUpVectorBar' : u'\u2954',
    'RightVector' : u'\u21C0',
    'RightVectorBar' : u'\u2953',
    'RoundImplies' : u'\u2970',
    'RoundSpaceIndicator' : u'\uF3B2',
    'Rule' : u'\uF522',
    'RuleDelayed' : u'\uF51F',
    'SadSmiley' : u'\u2639',
    'Sampi' : u'\u03E0',
    'Saturn' : u'\u2644',
    'ScriptA' : u'\uF6B2',
    'ScriptB' : u'\uF6B3',
    'ScriptC' : u'\uF6B4',
    'ScriptCapitalA' : u'\uF770',
    'ScriptCapitalB' : u'\u212C',
    'ScriptCapitalC' : u'\uF772',
    'ScriptCapitalD' : u'\uF773',
    'ScriptCapitalE' : u'\u2130',
    'ScriptCapitalF' : u'\u2131',
    'ScriptCapitalG' : u'\uF776',
    'ScriptCapitalH' : u'\u210B',
    'ScriptCapitalI' : u'\u2110',
    'ScriptCapitalJ' : u'\uF779',
    'ScriptCapitalK' : u'\uF77A',
    'ScriptCapitalL' : u'\u2112',
    'ScriptCapitalM' : u'\u2133',
    'ScriptCapitalN' : u'\uF77D',
    'ScriptCapitalO' : u'\uF77E',
    'ScriptCapitalP' : u'\u2118',
    'ScriptCapitalQ' : u'\uF780',
    'ScriptCapitalR' : u'\u211B',
    'ScriptCapitalS' : u'\uF782',
    'ScriptCapitalT' : u'\uF783',
    'ScriptCapitalU' : u'\uF784',
    'ScriptCapitalV' : u'\uF785',
    'ScriptCapitalW' : u'\uF786',
    'ScriptCapitalX' : u'\uF787',
    'ScriptCapitalY' : u'\uF788',
    'ScriptCapitalZ' : u'\uF789',
    'ScriptD' : u'\uF6B5',
    'ScriptDotlessI' : u'\uF730',
    'ScriptDotlessJ' : u'\uF731',
    'ScriptE' : u'\u212F',
    'ScriptEight' : u'\uF7F8',
    'ScriptF' : u'\uF6B7',
    'ScriptFive' : u'\uF7F5',
    'ScriptFour' : u'\uF7F4',
    'ScriptG' : u'\u210A',
    'ScriptH' : u'\uF6B9',
    'ScriptI' : u'\uF6BA',
    'ScriptJ' : u'\uF6BB',
    'ScriptK' : u'\uF6BC',
    'ScriptL' : u'\u2113',
    'ScriptM' : u'\uF6BE',
    'ScriptN' : u'\uF6BF',
    'ScriptNine' : u'\uF7F9',
    'ScriptO' : u'\u2134',
    'ScriptOne' : u'\uF7F1',
    'ScriptP' : u'\uF6C1',
    'ScriptQ' : u'\uF6C2',
    'ScriptR' : u'\uF6C3',
    'ScriptS' : u'\uF6C4',
    'ScriptSeven' : u'\uF7F7',
    'ScriptSix' : u'\uF7F6',
    'ScriptT' : u'\uF6C5',
    'ScriptThree' : u'\uF7F3',
    'ScriptTwo' : u'\uF7F2',
    'ScriptU' : u'\uF6C6',
    'ScriptV' : u'\uF6C7',
    'ScriptW' : u'\uF6C8',
    'ScriptX' : u'\uF6C9',
    'ScriptY' : u'\uF6CA',
    'ScriptZ' : u'\uF6CB',
    'ScriptZero' : u'\uF7F0',
    'Section' : u'\u00A7',
    'SelectionPlaceholder' : u'\uF527',
    'SHacek' : u'\u0161',
    'Sharp' : u'\u266F',
    'ShortLeftArrow' : u'\uF526',
    'ShortRightArrow' : u'\uF525',
    'Sigma' : u'\u03C3',
    'SixPointedStar' : u'\u2736',
    'SkeletonIndicator' : u'\u2043',
    'SmallCircle' : u'\u2218',
    'SpaceIndicator' : u'\u2423',
    'SpaceKey' : u'\uF7BF',
    'SpadeSuit' : u'\u2660',
    'SpanFromAbove' : u'\uF3BB',
    'SpanFromBoth' : u'\uF3BC',
    'SpanFromLeft' : u'\uF3BA',
    'SphericalAngle' : u'\u2222',
    'Sqrt' : u'\u221A',
    'Square' : u'\uF520',
    'SquareIntersection' : u'\u2293',
    'SquareSubset' : u'\u228F',
    'SquareSubsetEqual' : u'\u2291',
    'SquareSuperset' : u'\u2290',
    'SquareSupersetEqual' : u'\u2292',
    'SquareUnion' : u'\u2294',
    'Star' : u'\u22C6',
    'Sterling' : u'\u00A3',
    'Stigma' : u'\u03DB',
    'Subset' : u'\u2282',
    'SubsetEqual' : u'\u2286',
    'Succeeds' : u'\u227B',
    'SucceedsEqual' : u'\u2AB0',
    'SucceedsSlantEqual' : u'\u227D',
    'SucceedsTilde' : u'\u227F',
    'SuchThat' : u'\u220D',
    'Sum' : u'\u2211',
    'Superset' : u'\u2283',
    'SupersetEqual' : u'\u2287',
    'SystemEnterKey' : u'\uF75F',
    'SZ' : u'\u00DF',
    'TabKey' : u'\uF7BE',
    'Tau' : u'\u03C4',
    'THacek' : u'\u0165',
    'Therefore' : u'\u2234',
    'Theta' : u'\u03B8',
    'ThickSpace' : u'\u2005',
    'ThinSpace' : u'\u2009',
    'Thorn' : u'\u00FE',
    'Tilde' : u'\u223C',
    'TildeEqual' : u'\u2243',
    'TildeFullEqual' : u'\u2245',
    'TildeTilde' : u'\u2248',
    'Times' : u'\u00D7',
    'Trademark' : u'\u2122',
    'Transpose' : u'\uF3C7',
    'UAcute' : u'\u00FA',
    'UDoubleAcute' : u'\u0171',
    'UDoubleDot' : u'\u00FC',
    'UGrave' : u'\u00F9',
    'UHat' : u'\u00FB',
    'UnderBrace' : u'\uFE38',
    'UnderBracket' : u'\u23B5',
    'UnderParenthesis' : u'\uFE36',
    'Union' : u'\u22C3',
    'UnionPlus' : u'\u228E',
    'UpArrow' : u'\u2191',
    'UpArrowBar' : u'\u2912',
    'UpArrowDownArrow' : u'\u21C5',
    'UpDownArrow' : u'\u2195',
    'UpEquilibrium' : u'\u296E',
    'UpperLeftArrow' : u'\u2196',
    'UpperRightArrow' : u'\u2197',
    'UpPointer' : u'\u25B4',
    'Upsilon' : u'\u03C5',
    'UpTee' : u'\u22A5',
    'UpTeeArrow' : u'\u21A5',
    'Uranus' : u'\u2645',
    'URing' : u'\u016F',
    'Vee' : u'\u22C1',
    'Venus' : u'\u2640',
    'VerticalBar' : u'\u2223',
    'VerticalEllipsis' : u'\u22EE',
    'VerticalLine' : u'\u2502',
    'VerticalSeparator' : u'\uF432',
    'VerticalTilde' : u'\u2240',
    'VeryThinSpace' : u'\u200A',
    'WarningSign' : u'\uF725',
    'WatchIcon' : u'\u231A',
    'Wedge' : u'\u22C0',
    'WeierstrassP' : u'\u2118',
    'WhiteBishop' : u'\u2657',
    'WhiteKing' : u'\u2654',
    'WhiteKnight' : u'\u2658',
    'WhitePawn' : u'\u2659',
    'WhiteQueen' : u'\u2655',
    'WhiteRook' : u'\u2656',
    'Wolf' : u'\uF720',
    'Xi' : u'\u03BE',
    'Xnor' : u'\uF4A2',
    'Xor' : u'\u22BB',
    'YAcute' : u'\u00FD',
    'YDoubleDot' : u'\u00FF',
    'Yen' : u'\u00A5',
    'Zeta' : u'\u03B6',
    'ZHacek' : u'\u017E',
}
