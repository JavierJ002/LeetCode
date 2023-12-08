class Solution:
    def threeSum(self, nums):
        nums.sort()
        resp = []
        for i, x in enumerate(nums): 
          if i > 0 and x == nums[i - 1]:
              continue # si no es la primera posicion del arreglo y el numero anterior es igual que el valor de X actual, saltaté la vuelta
          j = i + 1
          k = len(nums) - 1
          while j < k: #Aplicacion del Two Sum clásico pero con el valor de x que es el primer item de la suma de 3 dígitos ya que y + z serán el inverso de xporque array en orden
            suma = x + nums[j] + nums[k] 
            if suma == 0:
              resp.append([x, nums[j], nums[k]])
              j += 1
              while nums[j] == nums[j - 1] and j < k: # actualizar el puntero con el fin de no obtener la misma resp en el append del arreglo final
                j += 1
            elif suma > 0:
              k -= 1
            else:
              j += 1
        return resp 
