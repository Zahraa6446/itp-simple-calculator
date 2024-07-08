{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRIxe+IQddkNXzy5e0ZUJl",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Zahraa6446/itp-simple-calculator/blob/master/Calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "b5JJ0mfdD4Tr"
      },
      "outputs": [],
      "source": [
        "def add(a,b):\n",
        "  return a+b\n",
        "\n",
        "def subtract(a,b):\n",
        "  return a-b\n",
        "\n",
        "def mul(a,b):\n",
        "  return a*b"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def divide(a,b):\n",
        "  if b>0 or b<0:\n",
        "    return a/b\n",
        "  else:\n",
        "    return 'invalid value for domenator, can\"t divide by 0'\n",
        "\n",
        "def sequare(a):\n",
        "  return a^2\n",
        "\n",
        "def power(a,b):\n",
        "  return a**b\n",
        "\n",
        "import math\n",
        "def sequare_root(a):\n",
        "  return math.sqrt(a)\n",
        "\n",
        "sequare_root(4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XZEoAWh8E4V1",
        "outputId": "58365a4e-7b83-4a48-d957-b9a0c859bba4"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2.0"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    }
  ]
}