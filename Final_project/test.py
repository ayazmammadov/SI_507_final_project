import unittest
import crawlimdb as main
import json
import requests

# Test

class TestMovieList(unittest.TestCase):

    def testConstructor1(self):
        m1 = main.MovieList('testMovieHref.com','testDirector','testActor', 'testMovieName','testReleaseDate','testPosterHref.com')
        self.assertEqual(m1.href, "testMovieHref.com")
        self.assertEqual(m1.dir, "testDirector")
        self.assertEqual(m1.actor, "testActor")
        self.assertEqual(m1.movieName, "testMovieName")
        self.assertEqual(m1.releaseDate, "testReleaseDate")
        self.assertEqual(m1.poster, "testPosterHref.com")

    def testConstrAndStr(self):
        m1 = main.MovieList('testMovieHref.com2','testDirector2','testActor2', 'testMovieName2','testReleaseDate2','testPosterHref.com2')
        self.assertEqual(m1.href, "testMovieHref.com2")
        self.assertEqual(m1.dir, "testDirector2")
        self.assertEqual(m1.actor, "testActor2")
        self.assertEqual(m1.movieName, "testMovieName2")
        self.assertEqual(m1.releaseDate, "testReleaseDate2")
        self.assertEqual(m1.poster, "testPosterHref.com2")
        self.assertEqual(str(m1),"the movie name is testMovieName2, directed bytestDirector2. The release date istestReleaseDate2. The main actor istestActor2. Genre is ")

    def testNotConstructorAndStr(self):
         m1 = main.MovieList('testMovieHref2.com','testDirector2','testActor2', 'testMovieName2','testReleaseDate2','testPosterHref.com2')
         self.assertNotEqual(m1.href, " ")
         self.assertNotEqual(m1.dir, "")
         self.assertNotEqual(m1.actor, "")
         self.assertNotEqual(m1.movieName, "")
         self.assertNotEqual(m1.releaseDate, "")
         self.assertNotEqual(m1.poster, "")
         self.assertNotEqual(str(m1),"")



unittest.main()
