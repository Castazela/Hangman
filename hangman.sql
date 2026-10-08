-- MySQL dump 10.13  Distrib 26.7.0, for macos27.0 (arm64)
--
-- Host: 127.0.0.1    Database: hangman
-- ------------------------------------------------------
-- Server version	9.7.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '52a164ac-c286-11f1-b483-8dfb44632388:1-11';

--
-- Table structure for table `game`
--

DROP TABLE IF EXISTS `game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `game` (
  `user_id` varchar(20) NOT NULL,
  `word_to_guess` text,
  `attempts_number` int DEFAULT NULL,
  `loose_win` tinyint(1) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `game`
--

LOCK TABLES `game` WRITE;
/*!40000 ALTER TABLE `game` DISABLE KEYS */;
/*!40000 ALTER TABLE `game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `words`
--

DROP TABLE IF EXISTS `words`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `words` (
  `mot` varchar(50) NOT NULL,
  `theme` text NOT NULL,
  PRIMARY KEY (`mot`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `words`
--

LOCK TABLES `words` WRITE;
/*!40000 ALTER TABLE `words` DISABLE KEYS */;
INSERT INTO `words` VALUES ('abricot','fruit_legume'),('accordéon','instrument'),('agriculteur','métier'),('aigle','animaux'),('Ajaccio','ville_française'),('Aladdin','personnage'),('Algérie','pays'),('Allemagne','pays'),('Amiens','ville_française'),('ananas','fruit_legume'),('Angers','ville_française'),('Angleterre','pays'),('Antibes','ville_française'),('architecte','métier'),('argenté','couleur'),('Argentine','pays'),('artichaut','fruit_legume'),('asperge','fruit_legume'),('assiette','objet'),('Astérix','personnage'),('athlétisme','sport'),('aubergine','fruit_legume'),('Australie','pays'),('Autriche','pays'),('Avignon','ville_française'),('aviron','sport'),('avocat','métier'),('badminton','sport'),('baleine','animaux'),('ballon','objet'),('Baloo','personnage'),('Bambi','personnage'),('banane','fruit_legume'),('basket','sport'),('basse','instrument'),('batterie','instrument'),('Bayonne','ville_française'),('beige','couleur'),('Belgique','pays'),('Besançon','ville_française'),('betterave','fruit_legume'),('Biarritz','ville_française'),('Bill','personnage'),('bison','animaux'),('blanc','couleur'),('bleu','couleur'),('Bordeaux','ville_française'),('boucher','métier'),('boulanger','métier'),('Boule','personnage'),('bouteille','objet'),('boxe','sport'),('Brésil','pays'),('Brest','ville_française'),('brocoli','fruit_legume'),('brosse','objet'),('Buzz','personnage'),('Caen','ville_française'),('Canada','pays'),('Cannes','ville_française'),('carotte','fruit_legume'),('castor','animaux'),('céleri','fruit_legume'),('Cendrillon','personnage'),('cerf','animaux'),('cerise','fruit_legume'),('chaise','objet'),('chameau','animaux'),('champignon','fruit_legume'),('cheval','animaux'),('Chili','pays'),('chimpanzé','animaux'),('Chine','pays'),('chou','fruit_legume'),('ciseaux','objet'),('citron','fruit_legume'),('clarinette','instrument'),('clé','objet'),('clémentine','fruit_legume'),('coiffeur','métier'),('Colombie','pays'),('concombre','fruit_legume'),('cornemuse','instrument'),('courgette','fruit_legume'),('couteau','objet'),('crocodile','animaux'),('Cuba','pays'),('cuillère','objet'),('cuisinier','métier'),('cyclisme','sport'),('cygne','animaux'),('Dalton','personnage'),('Danemark','pays'),('dauphin','animaux'),('dentiste','métier'),('Dijon','ville_française'),('Dingo','personnage'),('Donald','personnage'),('doré','couleur'),('Droopy','personnage'),('Dumbo','personnage'),('écarlate','couleur'),('écureuil','animaux'),('Égypte','pays'),('électricien','métier'),('éléphant','animaux'),('Elsa','personnage'),('épinard','fruit_legume'),('équitation','sport'),('escrime','sport'),('Espagne','pays'),('facteur','métier'),('fenouil','fruit_legume'),('figue','fruit_legume'),('Finlande','pays'),('flamant','animaux'),('flûte','instrument'),('football','sport'),('fourchette','objet'),('fraise','fruit_legume'),('framboise','fruit_legume'),('France','pays'),('Garfield','personnage'),('Gaston','personnage'),('girafe','animaux'),('golf','sport'),('gorille','animaux'),('Grèce','pays'),('grenade','fruit_legume'),('Grenoble','ville_française'),('gris','couleur'),('guépard','animaux'),('guitare','instrument'),('gymnastique','sport'),('handball','sport'),('haricot','fruit_legume'),('harmonica','instrument'),('harpe','instrument'),('hautbois','instrument'),('hérisson','animaux'),('hibou','animaux'),('hippopotame','animaux'),('horloge','objet'),('Inde','pays'),('indigo','couleur'),('infirmier','métier'),('Irlande','pays'),('Islande','pays'),('Italie','pays'),('Iznogoud','personnage'),('Japon','pays'),('jaune','couleur'),('Jerry','personnage'),('journaliste','métier'),('judo','sport'),('kaki','couleur'),('kangourou','animaux'),('karaté','sport'),('Kenya','pays'),('kiwi','fruit_legume'),('koala','animaux'),('lampe','objet'),('lapin','animaux'),('léopard','animaux'),('Lille','ville_française'),('Limoges','ville_française'),('lion','animaux'),('litchi','fruit_legume'),('loup','animaux'),('loutre','animaux'),('lunettes','objet'),('lynx','animaux'),('Lyon','ville_française'),('Madagascar','pays'),('mandarine','fruit_legume'),('mangue','fruit_legume'),('Mario','personnage'),('Maroc','pays'),('marron','couleur'),('Marseille','ville_française'),('Marsupilami','personnage'),('mauve','couleur'),('mécanicien','métier'),('médecin','métier'),('melon','fruit_legume'),('menuisier','métier'),('Metz','ville_française'),('Mexique','pays'),('Mickey','personnage'),('Milou','personnage'),('Minnie','personnage'),('miroir','objet'),('Montpellier','ville_française'),('montre','objet'),('morse','animaux'),('Mowgli','personnage'),('Mulhouse','ville_française'),('myrtille','fruit_legume'),('Nancy','ville_française'),('Nantes','ville_française'),('natation','sport'),('navet','fruit_legume'),('Nemo','personnage'),('Nice','ville_française'),('Nîmes','ville_française'),('noir','couleur'),('Norvège','pays'),('Obélix','personnage'),('ocre','couleur'),('oignon','fruit_legume'),('orange','fruit_legume'),('Orléans','ville_française'),('ours','animaux'),('pamplemousse','fruit_legume'),('panda','animaux'),('panthère','animaux'),('parapluie','objet'),('Paris','ville_française'),('pastèque','fruit_legume'),('pêche','fruit_legume'),('Pérou','pays'),('Perpignan','ville_française'),('perroquet','animaux'),('phoque','animaux'),('piano','instrument'),('pieuvre','animaux'),('Pikachu','personnage'),('pilote','métier'),('pingouin','animaux'),('Pinocchio','personnage'),('plombier','métier'),('Pluto','personnage'),('poire','fruit_legume'),('poireau','fruit_legume'),('Poitiers','ville_française'),('poivron','fruit_legume'),('policier','métier'),('Pologne','pays'),('pomme','fruit_legume'),('pompier','métier'),('Popeye','personnage'),('Portugal','pays'),('potiron','fruit_legume'),('pourpre','couleur'),('professeur','métier'),('prune','fruit_legume'),('radis','fruit_legume'),('raisin','fruit_legume'),('Rantanplan','personnage'),('Reims','ville_française'),('renard','animaux'),('Rennes','ville_française'),('requin','animaux'),('rhinocéros','animaux'),('rose','couleur'),('Roubaix','ville_française'),('Rouen','ville_française'),('rouge','couleur'),('rugby','sport'),('Russie','pays'),('sanglier','animaux'),('saxophone','instrument'),('Sénégal','pays'),('serpent','animaux'),('Shrek','personnage'),('Simba','personnage'),('singe','animaux'),('ski','sport'),('Snoopy','personnage'),('Sonic','personnage'),('Spirou','personnage'),('Strasbourg','ville_française'),('stylo','objet'),('Suède','pays'),('Suisse','pays'),('surf','sport'),('synthétiseur','instrument'),('table','objet'),('tambour','instrument'),('tapis','objet'),('Tarzan','personnage'),('tennis','sport'),('Thaïlande','pays'),('tigre','animaux'),('Tintin','personnage'),('Tom','personnage'),('tomate','fruit_legume'),('tortue','animaux'),('Toulon','ville_française'),('Toulouse','ville_française'),('Tours','ville_française'),('trombone','instrument'),('trompette','instrument'),('Tunisie','pays'),('Turquie','pays'),('turquoise','couleur'),('ukulélé','instrument'),('valise','objet'),('vert','couleur'),('Vietnam','pays'),('Villeurbanne','ville_française'),('violet','couleur'),('violon','instrument'),('violoncelle','instrument'),('volley','sport'),('Woody','personnage'),('xylophone','instrument'),('zèbre','animaux'),('Zorro','personnage');
/*!40000 ALTER TABLE `words` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-08 10:06:27
